# Initial issue backlog

These tasks are ready to copy into GitHub Issues; the file itself does not create issues.

## RB-T01 — Freeze coordinate frames and preliminary geometry

- [ ] Define base/shoulder offsets, joint axes, signs and zero poses.
- [ ] Record link dimensions and provisional joint limits.
- [ ] Compare idealized helper conventions with CAD.

Acceptance: a reviewed frame diagram and forward-kinematics convention are committed.

## RB-T02 — Reconcile motor selection and transmission sizing

- [ ] Resolve inconsistent motor/model/ratio labels in the proposal.
- [ ] Use CAD mass properties and intended accelerations.
- [ ] Document torque, speed, current and mechanical margins.

Acceptance: one actuator/ratio/driver matrix supports procurement.

## RB-T03 — Build the dynamic model and baseline simulation

- [ ] Specify masses, inertia, friction, transmission and actuator model.
- [ ] Run one named reference trajectory with a fixed baseline controller.
- [ ] Save parameters, script/model version and expected outputs.

Acceptance: a team member can reproduce nominal and variable-load baseline runs.

## RB-T04 — Derive and simulate the MRAC law

- [ ] Define reference model, adaptive parameters, equations and assumptions.
- [ ] Include parameter bounds, actuator saturation and noise cases.
- [ ] Compare against the baseline with matched limits and trials.

Acceptance: equations, configurations and bounded-behavior evidence are reviewed.

## RB-T05 — Verify one-joint sensing, drive limits and timing

- [ ] Calibrate encoder/current measurements under reviewed bench conditions.
- [ ] Verify limits and stop behavior before motion trials.
- [ ] Measure control period, execution time, jitter and overruns.

Acceptance: publish a sanitized bench log with the actual achieved timing.

## RB-T06 — Define payload-change and recovery protocol

- [ ] Freeze trajectory, speed, payload event and recovery band/dwell.
- [ ] Define encoder-derived versus externally measured Cartesian error.
- [ ] Specify repeated runs and comparison procedure.

Acceptance: the protocol is written before reporting 5 mm or 0.5 s performance.

## RB-T07 — Select and validate the interaction layer

- [ ] Choose impedance/admittance structure supported by the hardware.
- [ ] Define force measurement/observer limits and calibration.
- [ ] Review the MRAC/interaction interconnection and contact-test conditions.

Acceptance: control and measurement claims match the implemented architecture.

## RB-T08 — Publish the first measured experiment

- [ ] Include real setup photo and public-safe versioned logs.
- [ ] Add path/error/current/parameter plots and trial counts.
- [ ] Record achieved metrics, failed targets and personal contributions.

Acceptance: the published experiment is reproducible and distinct from simulation/CAD.
