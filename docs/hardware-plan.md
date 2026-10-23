# Preliminary mechanical and electronic plan

| Area | Proposal direction | Decision/evidence required |
| --- | --- | --- |
| Geometry | 150 mm and 120 mm links | Actual offsets, center of mass, limits, and CAD mass properties |
| Structure | FDM PLA+, standard shaft/bearings/fasteners | Print orientation, fit, stiffness, and deflection checks |
| Base actuation | Geared DC motor with encoder | Resolve exact part, gearbox ratio, torque/speed/current data |
| Shoulder/elbow | DC gearmotors plus belt/pulley stages | Reconcile combined gearbox/belt ratios, torque margin, speed and backlash |
| Candidate belt ratios | J2 about 4:1–8:1; J3 about 4:1–6:1 | Size tooth count, belt width/tension, and bearing loads |
| Joint sensing | 12–14 bit magnetic absolute encoders; integrated encoder option on J1 | Interface/timing, placement, zero reference, calibration and error |
| Current sensing | Three shunt/amplifier channels | Range, bandwidth, offset, noise and motor-current calibration |
| Controller | STM32H7-class MCU | Exact board, peripherals, pin budget and toolchain |
| Drive/power | Bidirectional H-bridges, nominal 24 V system | Continuous/peak current, current-control capability, regeneration and protection |
| Stop/limits | E-stop, fuse, joint/current/speed limits | Reviewed fault path and bench evidence |

The proposal narrative and budget do not identify a fully consistent set of final motor model/speed/ratio labels. Keep procurement choices open until datasheets and sizing are reconciled. A motor's nominal RPM is not a joint-speed specification after transmission.

## Preliminary payload torque check

At horizontal full extension, the 0.100 kg payload alone gives approximately `0.100 × 9.81 × 0.270 ≈ 0.265 N·m` at the shoulder and `0.100 × 9.81 × 0.120 ≈ 0.118 N·m` at the elbow.

These values exclude link/drive mass, acceleration, friction, belt losses, transmission inertia and design margin. The proposal estimates roughly 0.5–0.6 N·m shoulder and 0.15 N·m elbow static torque after preliminary additions; final sizing must use actual CAD masses and dynamic cases.

Budget numbers are procurement-stage estimates and are omitted from the public README. Refresh them from actual quotations if a budget is later published.
