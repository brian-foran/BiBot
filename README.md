# BiBot

BiBot is my Master's thesis project: a fully custom-built bipedal robot whose dynamic control will be developed through reinforcement learning.

This repository is both the engineering workspace and the evidence trail for the project. Keep dated notes on what was tried, what happened, and why decisions were made. Those records should make it possible to explain the engineering journey in the thesis and portfolio without relying on memory.

## Repository map

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
	portfolio/                Portfolio story sourced from project evidence
	thesis/                   Thesis outline and evidence pointers
```

## Working conventions

- Record meaningful work in `docs/journal/` while details are fresh. Include links to relevant CAD, code, photos, measurements, or experiment records.
- When choosing between alternatives or changing direction, add a dated record using `docs/decisions/template.md`. Capture the context, options, rationale, and consequences, including uncertainty.
- Give each experiment a clear question, setup, procedure, and result using `docs/experiments/template.md`. Link the decision or journal entry it informs.
- Keep technical source artifacts in the relevant `engineering/` area. Its README describes what belongs there and what evidence to capture.
- Treat `docs/thesis/` and `docs/portfolio/` as curated views of the evidence, not as the only place the underlying rationale is recorded.

## Project status

The repository is at the project-setup stage. Update this section as the build progresses, and link to the current roadmap or major milestone when one is established.
