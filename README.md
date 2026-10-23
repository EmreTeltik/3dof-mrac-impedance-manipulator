# 3-DOF Robotic Arm with MRAC and Impedance Control

[Türkçe açıklama](README.tr.md) · [Current status](STATUS.md) · [Roadmap](ROADMAP.md) · [Validation plan](docs/validation-plan.md)

An Ege University undergraduate thesis project to design and experimentally evaluate a compact 3-DOF robotic arm under variable payloads, combining Model Reference Adaptive Control (MRAC) with an impedance-control layer.

**Project status:** thesis proposal prepared; project at an initial development stage. A TÜBİTAK **2209-A application is planned**. No support approval is claimed. This initial repository contains the public design summary, targets, control architecture, verification plan, and an idealized kinematics utility; physical robot performance has not yet been demonstrated here.

## Engineering objective

The project will investigate how a manipulator responds to a changing end-effector payload and whether adaptation can bring its tracking response back toward a reference-model response. A complementary impedance layer is intended to shape interaction behavior through virtual mass, damping, and stiffness during controlled low-speed experiments.

## Proposed architecture

![Proposed real-time control architecture](docs/media/architecture.svg)

The preliminary robot has a yaw joint at the base and shoulder/elbow pitch joints. The proposal uses a geared base drive and belt/pulley transmission stages for the shoulder and elbow, with joint sensing and motor-current measurements feeding an STM32H7-class controller. Exact actuators, ratios, and the MRAC/impedance interconnection remain design decisions.

## Preliminary targets

All values below are **design or validation targets**, not achieved measurements.

| Item | Proposal target |
| --- | --- |
| Degrees of freedom | 3 rotational joints: J1 yaw, J2 pitch, J3 pitch |
| Nominal reach | 270 mm |
| Link lengths | 150 mm + 120 mm preliminary geometry |
| Nominal payload | 100 g |
| Real-time control rate | ≥500 Hz minimum target; 1 kHz desired |
| Joint-angle numerical resolution | ≤0.1° target; physical accuracy requires separate validation |
| Nominal Cartesian tracking | RMSE ≤5 mm target |
| Recovery after payload change | ≤0.5 s target under a predefined recovery rule |
| Structure | FDM-printed PLA+ and standard mechanical parts |
| Embedded controller | STM32H7-class candidate |
| Modeling and analysis | MATLAB/Simulink planned |

The 270 mm reach is a nominal geometric value, not a claim that the full sphere is mechanically reachable or suitable for tracking. Joint limits, offsets, singularities, deflection, backlash, and torque limits will restrict the usable workspace.

## Planned development

1. Define coordinate frames, physical constraints, reference trajectories, and test metrics.
2. Build kinematic and dynamic models and size actuators using actual CAD mass properties.
3. Validate a conventional baseline controller and a reference model in simulation.
4. Develop the MRAC law, parameter bounds, saturation handling, and stability argument for the actual plant/control structure.
5. Integrate the embedded acquisition and drive system; verify timing, limits, and E-stop independently.
6. Evaluate sudden and gradual payload changes with synchronized angle/current logs.
7. Add the impedance layer and evaluate the combined system under controlled interaction conditions.

## Planned evaluation scenarios

| Scenario | Quantities to record |
| --- | --- |
| Fixed nominal payload and reference trajectory | Cartesian/joint error, RMS/peak current, tracking limits |
| Sudden payload change | Error envelope, recovery time, current peak, adaptive parameter bounds |
| Gradual payload change | Tracking trends, parameter evolution, current response |
| Baseline versus MRAC | Paired error/timing metrics under the same operating limits |
| Impedance interaction | Reference displacement, actual displacement, current; force only if measured/calibrated |
| Timing and fault handling | Cycle period, execution time, overruns, sensor faults, controlled shutdown |

Motor current alone is not a calibrated end-effector force measurement. The force-observation method and the distinction between impedance and admittance implementations must be resolved before making contact-performance claims.

## Try the included idealized kinematics tool

The starter tool uses only the Python standard library:

```bash
python tools/kinematics_preview.py --angles-deg 0 30 -45
python -m unittest discover -s tests -v
```

Python 3.10+ is sufficient. Windows may use `py` instead of `python`. The tool provides forward kinematics, an analytic Jacobian, and a limited inverse-kinematics helper for an explicitly defined ideal yaw-pitch-pitch geometry. It is not a dynamic simulation, MRAC implementation, motor driver, or verification of the final mechanical design. MATLAB/Simulink remains the planned modeling environment.

## Documentation

| Document | Purpose |
| --- | --- |
| [Requirements](docs/requirements.md) | Targets and required evidence |
| [Architecture](docs/architecture.md) | Control, sensing, timing, and drive boundaries |
| [Kinematics](docs/kinematics.md) | Coordinate conventions and idealized starter equations |
| [Hardware plan](docs/hardware-plan.md) | Mechanical, actuator, encoder, driver, and power decisions |
| [Control plan](docs/control-plan.md) | MRAC/reference model and impedance-development questions |
| [Validation plan](docs/validation-plan.md) | Baselines, load changes, timing, and interaction tests |
| [Open decisions](docs/open-decisions.md) | Unresolved technical choices |
| [Backlog](docs/backlog.md) | Tasks ready to convert into GitHub Issues |
| [Contributors](CONTRIBUTORS.md) | Thesis authors, advisor, and contribution tracking |

## Team

**Thesis authors:** Emre Teltik and Mehmet Can Tanürün. **Advisor:** Dr. Erman Selim. Individual implementation responsibilities will be recorded as work is allocated and performed.

## Evidence and current limits

No physical robot test, measured tracking score, recovery-time result, or combined-controller stability proof is included in this initial version. The project will use relevant robot/machinery safety principles as design references; this repository does not claim a certified collaborative robot or verified standard compliance. Original proposal pages with student IDs and contact details are excluded from this public package. Public release and licensing will be coordinated with the authors and advisor.
