# BiBot

BiBot is my Master's thesis project: a fully custom-built bipedal robot whose dynamic control will be developed through reinforcement learning.

This repository is both the engineering workspace and the evidence trail for the project. Beyond being my note-keeping repo for the eventual theis paper, I want this to serve as a log book for the planning, decisions, setbacks, and achievements that occur when pursuing a large-scale engineering project.

## TODO
Live list of action items. Once completed, record in /docs and remove

* Mechanical
    
    * Design new legs in Autocad
    * Buy new servos, etc

* Electrical

    * Investigate potentiometers for feedback
    * But perfboard supplies

* Firmware

    * Make Nano the Master
    * Broadcast all state info (servo pos, gyro, accel to ESP)
    * Figure out ESP messaging to master using interupt for web control
    * Store live data on laptop / rpi using esp wifi

## Material and Budget

See here for the live budget with links to materials: [BUDGET](https://docs.google.com/spreadsheets/d/1oGoLCpEEcJNgCdJp1yFPbvFVYQjBTa5PGdgrq4-x1HY/edit?usp=sharing)

This robot could be made at its cheapest for $40. Better motors, spare parts, and complex test rigs could raise this price significantly.


# Repo Info
## Directory map

```text
engineering/
	control/                 Control approach, simulation, and reinforcement learning
	electrical/              Servos, controllers, modules, wiring, and power
	firmware/                On-board software and bring-up notes
	mechanical/frame/        Robot frame CAD, fabrication, and 3D-print records
docs/
	decisions/               Decision log and individual decision records
	experiments/              Reproducible tests and results
	journal/                  Dated build notes and challenges
	thesis/                   Thesis outline and evidence pointers
```

## Working conventions

- Record meaningful work in `docs/journal/` while details are fresh. Include links to relevant CAD, code, photos, measurements, or experiment records.
- When choosing between alternatives or changing direction, add a dated record using `docs/decisions/template.md`. Capture the context, options, rationale, and consequences, including uncertainty.
- Give each experiment a clear question, setup, procedure, and result using `docs/experiments/template.md`. Link the decision or journal entry it informs.
- Keep technical source artifacts in the relevant `engineering/` area. Its README describes what belongs there and what evidence to capture.
- Treat `docs/thesis/` and `docs/portfolio/` as curated views of the evidence, not as the only place the underlying rationale is recorded.

## Project status

The project is early in the development state. I am determining scope and feasability now, which are likely to change
