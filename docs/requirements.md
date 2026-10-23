# Preliminary requirements

| ID | Proposal requirement / target | Verification evidence | State |
| --- | --- | --- | --- |
| RB-01 | Three rotational joints | Assembly and joint-command demonstration | Planned |
| RB-02 | 270 mm nominal reach, ±5 mm target tolerance | Dimensioned CAD and physical measurement | Planned |
| RB-03 | 100 g nominal payload | Reviewed static/dynamic sizing and controlled load test | Planned |
| RB-04 | ≥500 Hz loop, 1 kHz desired | Execution-time/period/jitter/deadline logs | Planned |
| RB-05 | ≤0.1° numerical joint resolution | Encoder chain calculation; physical accuracy measured separately | Planned |
| RB-06 | Cartesian tracking RMSE ≤5 mm | Defined reference, position estimation/measurement method and paired timestamps | Planned |
| RB-07 | Recovery ≤0.5 s after load change | Predefined error threshold, dwell time, event timestamp and recorded response | Planned |
| RB-08 | Bounded adaptive parameters | Adaptation-state, saturation and error logs | Planned |
| RB-09 | Joint/current/speed limits and E-stop | Independent fault/stop checks under controlled bench conditions | Planned |
| RB-10 | Adjustable interaction behavior | Defined impedance/admittance structure and calibrated measurement method | Planned |

Physical interaction tests are downstream of protection and controllability verification. Relevant safety standards are proposal design references, not certifications awarded to this prototype.
