# Idealized kinematics starter utility

From the repository root with Python 3.10+:

```bash
python tools/kinematics_preview.py --angles-deg 0 30 -45
python -m unittest discover -s tests -v
```

Windows can use `py` instead of `python`. There are no third-party dependencies. The CLI prints its idealized geometry label, input angles, position in metres, and Jacobian in m/rad. The Python module also exposes an inverse-kinematics helper for the nonnegative radial branch and rejects base-axis ambiguity.

Read the coordinate definitions in `docs/kinematics.md`. Joint limits, actual offsets, collisions, flex, transmissions, dynamics, actuator commands, adaptation and contact are not modeled. Use this tool for early math checks; it is not a robot controller.
