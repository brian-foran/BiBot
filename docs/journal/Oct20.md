# 2026-10-20: Esp Testing

## Goal
Start testing the limits of ESP -> Host communication to see what frequency of states we can communicate 

## Work completed

Created esp_frequency_test.py and matching .ino file for esp to test the frequency limit. See below for call syntax and results:

```text
python esp_listener.py 192.168.1.13 --rates 100,500,1000,2000,0 --batch 1 
```

```text
Testing rate=100 Hz batch=1 for 5.0s
      79 pkt/s       79 samp/s  lost so far: 0
     101 pkt/s      101 samp/s  lost so far: 0
      95 pkt/s       95 samp/s  lost so far: 0
     103 pkt/s      103 samp/s  lost so far: 0
  -> target 100 Hz, batch 1: received 96 samp/s (96 pkt/s, 3 KB/s), ESP-side 100 samp/s, loss 0.00% (0/479)
Testing rate=500 Hz batch=1 for 5.0s
     444 pkt/s      444 samp/s  lost so far: 0
     483 pkt/s      483 samp/s  lost so far: 0
     511 pkt/s      511 samp/s  lost so far: 0
     506 pkt/s      506 samp/s  lost so far: 0
  -> target 500 Hz, batch 1: received 489 samp/s (489 pkt/s, 15 KB/s), ESP-side 500 samp/s, loss 0.00% (0/2427)
Testing rate=1000 Hz batch=1 for 5.0s
     957 pkt/s      957 samp/s  lost so far: 5
     997 pkt/s      997 samp/s  lost so far: 9
     960 pkt/s      960 samp/s  lost so far: 28
     975 pkt/s      975 samp/s  lost so far: 70
  -> target 1000 Hz, batch 1: received 976 samp/s (976 pkt/s, 31 KB/s), ESP-side 1000 samp/s, loss 1.59% (79/4960)
Testing rate=2000 Hz batch=1 for 5.0s
    1324 pkt/s     1324 samp/s  lost so far: 634
    1585 pkt/s     1585 samp/s  lost so far: 1070
    1422 pkt/s     1422 samp/s  lost so far: 1591
    1546 pkt/s     1546 samp/s  lost so far: 2084
  -> target 2000 Hz, batch 1: received 1488 samp/s (1488 pkt/s, 47 KB/s), ESP-side 1999 samp/s, loss 25.44% (2539/9980)
Testing rate=0 Hz batch=1 for 5.0s
    1612 pkt/s     1612 samp/s  lost so far: 5891
    1378 pkt/s     1378 samp/s  lost so far: 13088
    1336 pkt/s     1336 samp/s  lost so far: 20321
    1374 pkt/s     1374 samp/s  lost so far: 27450
  -> target max Hz, batch 1: received 1444 samp/s (1444 pkt/s, 45 KB/s), ESP-side 8384 samp/s, loss 82.61% (34279/41497)
  
```

```text
 python .\esp_frequency_test.py  192.168.1.13 --rates 5000 --batch 20
Testing rate=5000 Hz batch=20 for 5.0s
     245 pkt/s     4900 samp/s  lost so far: 0
     245 pkt/s     4900 samp/s  lost so far: 80
     248 pkt/s     4960 samp/s  lost so far: 80
     243 pkt/s     4860 samp/s  lost so far: 80
  -> target 5000 Hz, batch 20: received 4944 samp/s (247 pkt/s, 154 KB/s), ESP-side 4978 samp/s, loss 0.32% (80/24760)
```

## Observations
More testing will be needed, but 500 samples/sec seems to be the limit when using a single sample per packet. However, we can recieve much more samples per second if we queue them into packets. Thus, the true limit comes from onboard memory limit.

## Decisions or open questions
- Decision records: 
    * Decided to remove using Eduroam as a goal. Not worth the trouble, will use hot spot if needed. 
    * I designed the PCB in KiCad, but realized that Spain PCB costs are too high to justify for a simple design. Switching to perfboard

- Questions to resolve: 
    * Is the discovered communication frequency sufficient for use case
    * Can this speed be maintained if also running a https page from the esp

## Evidence

## Next steps
- Take a look at the mmrp git repo shared from tim shumann. Bachelor's thesis of similar topic