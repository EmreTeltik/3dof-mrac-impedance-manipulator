# Development roadmap

| Milestone | Deliverables | Exit condition |
| --- | --- | --- |
| M0 — Definition | Public scope, requirements, initial architecture | Team reviews scope and allocation |
| M1 — Mechanical and kinematic model | CAD, frame definitions, workspace and torque sizing | Dimensions, mass properties, and actuator candidates reconciled |
| M2 — Baseline simulation | Dynamic model, reference trajectory, conventional controller | Reproducible nominal and variable-load simulations |
| M3 — MRAC simulation | Reference model, control/adaptation laws, bounds and saturation handling | Reviewed assumptions, baseline comparison, bounded behavior in planned cases |
| M4 — Electronics and one-joint tests | Sensing, driver interface, power protection, timing logs | Independent limits/E-stop and controlled bench tests |
| M5 — Three-joint prototype | Mechanical assembly, embedded loop, synchronized logging | Repeatable low-energy nominal tracking |
| M6 — Load-change experiments | Fixed/step/ramp payload tests | Paired baseline/MRAC logs and quantified results |
| M7 — Impedance integration | Reviewed interaction architecture and measurement method | Controlled experiments with defined force/position evidence |
| M8 — Final portfolio | Sanitized CAD/photos, scripts, plots, demo, thesis summary | Claims traceable to experiments and actual contributions |

## Initial checklist

- [x] Initial public design summary and validation plan prepared.
- [x] Idealized kinematics utility and consistency tests supplied.
- [ ] Review public summary and team attribution.
- [ ] Reconcile actuators, ratios, encoders, geometry, and mass assumptions.
- [ ] Complete the 2209-A application process and update actual status.
- [ ] Develop the dynamic model and baseline control simulation.
- [ ] Derive and evaluate the MRAC law.
- [ ] Verify one-joint hardware, protection, and timing.
- [ ] Integrate three joints and run payload experiments.
- [ ] Define and evaluate impedance interaction.

No thesis deadline or funder milestone is inferred from this sequence. Update it using the team's actual schedule.
