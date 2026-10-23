# Open engineering decisions

| ID | Question | Closure evidence |
| --- | --- | --- |
| D01 | What are final motor models and combined transmission ratios? | Reconciled datasheets, torque/speed/current sizing |
| D02 | What are actual base/shoulder offsets, joint limits and CAD masses? | Dimensioned model and mass-property export |
| D03 | How is joint velocity estimated and filtered? | Noise/delay study and implementation specification |
| D04 | Does each selected driver support the intended current/torque loop? | Driver architecture and measured bench behavior |
| D05 | Which exact MRAC parameterization and adaptation law will be used? | Derivation, assumptions and reproducible baseline comparison |
| D06 | Is the interaction layer torque-based impedance or force-to-motion admittance/reference shaping? | Signal diagram and actuator/measurement compatibility |
| D07 | How will external contact force be measured or estimated? | Sensor/observer calibration or explicitly limited evaluation claim |
| D08 | What error band and dwell time define recovery? | Written protocol before final experiments |
| D09 | How will Cartesian position be independently validated? | Measurement method, calibration and error budget |
| D10 | How are individual tasks allocated and public release approved by the team? | Updated contribution record and publication decision |

These are expected design questions at proposal stage. Close them with evidence rather than replacing them with unverified completion statements.
