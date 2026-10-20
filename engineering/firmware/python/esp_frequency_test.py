#!/usr/bin/env python3
"""Host side of the BiBot UDP rate test.

Examples:
  python host_udp_rate_test.py 192.168.43.50                      # 1 kHz, batch 1, 5 s
  python host_udp_rate_test.py 192.168.43.50 --rates 100,500,1000,2000,0 --batch 1
  python host_udp_rate_test.py 192.168.43.50 --rates 0 --batch 20  # max throughput, batched
Rate 0 = ESP sends as fast as it can.
"""
import argparse, socket, struct, time

SAMPLE = struct.Struct("<II12h")   # seq, t_us, 6 servo, 3 gyro, 3 accel (32 B)
ESP_PORT = 4210

def run(sock, esp, rate, batch, duration):
    sock.sendto(struct.pack("<IB", rate, batch), esp)   # start; also tells ESP our address
    buf = bytearray(2048)
    expected = None
    pkts = samples = lost = bytes_rx = 0
    first_t = last_t = None
    last_seq = last_esp_t = 0
    first_seq = first_esp_t = None
    t_end = time.perf_counter() + duration
    t_rep = time.perf_counter() + 1.0
    p_rep = s_rep = 0

    while True:
        now = time.perf_counter()
        if now >= t_end:
            break
        try:
            n, _ = sock.recvfrom_into(buf)
        except socket.timeout:
            continue
        if last_t is None or first_t is None:
            first_t = now
        last_t = now
        pkts += 1
        bytes_rx += n
        k = n // 32
        seq0, t0 = struct.unpack_from("<II", buf, 0)
        seqN, tN = struct.unpack_from("<II", buf, (k - 1) * 32)
        if expected is not None and seq0 != expected:
            lost += (seq0 - expected) & 0xFFFFFFFF
        if first_seq is None:
            first_seq, first_esp_t = seq0, t0
        expected = (seqN + 1) & 0xFFFFFFFF
        last_seq, last_esp_t = seqN, tN
        samples += k
        if now >= t_rep:
            print(f"  {pkts-p_rep:6d} pkt/s  {samples-s_rep:7d} samp/s  lost so far: {lost}")
            p_rep, s_rep, t_rep = pkts, samples, t_rep + 1.0

    sock.sendto(struct.pack("<IB", 0, 0), esp)   # stop
    time.sleep(0.2)
    try:                                         # drain stragglers
        while True:
            sock.recvfrom_into(buf)
    except socket.timeout:
        pass

    if not pkts or first_t is None or last_t is None or last_t == first_t:
        print("  no data received (check IP, firewall, same network)")
        return
    dt = last_t - first_t
    sent = last_seq - first_seq + 1
    esp_dt = ((last_esp_t - first_esp_t) & 0xFFFFFFFF) / 1e6
    print(f"  -> target {'max' if rate == 0 else rate} Hz, batch {batch}: "
          f"received {samples/dt:.0f} samp/s ({pkts/dt:.0f} pkt/s, {bytes_rx/dt/1024:.0f} KB/s), "
          f"ESP-side {sent/esp_dt if esp_dt else 0:.0f} samp/s, "
          f"loss {100*lost/max(sent,1):.2f}% ({lost}/{sent})")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("esp_ip")
    ap.add_argument("--rates", default="1000", help="comma list of Hz, 0 = unlimited")
    ap.add_argument("--batch", type=int, default=1, help="samples per UDP packet (1-40)")
    ap.add_argument("--duration", type=float, default=5.0, help="seconds per rate")
    a = ap.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4 * 1024 * 1024)
    sock.bind(("0.0.0.0", 0))
    sock.settimeout(0.5)
    esp = (a.esp_ip, ESP_PORT)

    for r in (int(x) for x in a.rates.split(",")):
        print(f"Testing rate={r} Hz batch={a.batch} for {a.duration}s")
        run(sock, esp, r, max(1, min(a.batch, 40)), a.duration)

if __name__ == "__main__":
    main()