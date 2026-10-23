# MRAC and interaction-control development plan

## Plant and baseline first

Define joint coordinates, actuator input, measurements, filtering, sample time, current-loop behavior, transmission model, friction, saturation and payload parameters. Establish a conventional baseline controller under the same limits before comparing adaptation.

The planned manipulator model is of the form `M(q)*q_ddot + C(q,q_dot)*q_dot + g(q) + friction = joint_torque + external_torque`. Model structure, parameterization, joint coupling and motor dynamics still require derivation and validation.

## Reference model and MRAC

Specify the desired model response, adaptive parameters, measured/estimated signals, adaptation law, gain selection, parameter bounds, and robustness modifications. The proposal calls for a Lyapunov-based approach. A valid stability argument must refer to the actual model assumptions and implemented interconnection.

Resolve how saturation, rate limits, measurement noise, velocity estimation, discrete implementation, numerical errors and payload changes affect adaptation. Parameter projection, dead zones or other modifications are candidates to study, not verified implementations in this repository.

## Impedance layer

The intended interaction relationship is a virtual mass–damping–stiffness behavior, commonly described using position error and external force. Decide whether the hardware supports a torque-based impedance loop or a force-to-motion admittance/reference-shaping loop. Name the implementation accurately.

The proposal's reference-shaping diagram does not by itself establish a physically implemented impedance controller. A calibrated force sensor, a validated force observer, or a more limited current/position-based evaluation must be chosen explicitly. Do not claim direct force regulation or certified collaborative operation from motor-current logs alone.

## Combined system

MRAC and impedance/admittance cannot be treated as independently verified blocks whose combination is automatically stable. Define their signal interconnection, relative rates, adaptation behavior during contact, saturation path, and energy/interaction constraints. Evaluate the combined configuration separately from free-space MRAC.

## Required evidence before an implementation claim

- A documented model and reference model.
- Explicit equations and software mapping for control/adaptation.
- Reproducible simulations against a fixed baseline.
- Logged parameter bounds, saturation, errors and timing.
- Controlled hardware validation matching the modeled conditions, with limitations reported.
