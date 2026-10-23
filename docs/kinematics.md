# Idealized starter kinematics

The helper is a deliberately simplified mathematical model, proposed for early consistency checks. It is not extracted from a final CAD or calibrated robot.

## Coordinate convention

The shoulder origin coincides with the base origin; all base/shoulder offsets are zero. The world z-axis is vertical. Joint q1 rotates about z. Positive q2 raises the first link from the horizontal radial direction. Joint q3 is the relative elbow angle in the same vertical plane. Zero angles place both links along world +x.

Use metres and radians internally. The starter values are `L2=0.150 m` and `L3=0.120 m`. The forward map is defined as:

```text
r = L2*cos(q2) + L3*cos(q2+q3)
x = r*cos(q1)
y = r*sin(q1)
z = L2*sin(q2) + L3*sin(q2+q3)
```

The analytic Jacobian is the derivative of this map with respect to `(q1,q2,q3)` and has units m/rad. This sign convention must be reconciled with physical encoder/motor signs before hardware use.

## Inverse helper limitations

For a nonnegative radial branch `rho=sqrt(x*x+y*y)`, the helper uses `q1=atan2(y,x)` and the planar two-link law of cosines. It provides elbow-positive and elbow-negative mathematical branches, without joint limits, collisions, transmission offsets, or dynamics. Points on the z-axis are rejected because base yaw is underdetermined. Other radial-sign branches and robot-specific offsets are not implemented.

For the ideal geometry, shoulder-to-tip distance must lie between `|L2-L3|` and `L2+L3`. This distance bound is necessary but not a physical reachability guarantee. Straight/folded elbow and zero radial projection create singular configurations for the Jacobian.

## Planned upgrade to the real model

1. Freeze actual coordinate frames, link offsets, joint limits and encoder zero references.
2. Derive transforms from dimensioned CAD and check representative physical configurations.
3. Compare analytic Jacobian values with finite differences.
4. Add workspace, collision, speed and torque constraints before generating motion commands.
5. Keep the idealized helper labelled separately if the final geometry differs.
