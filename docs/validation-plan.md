# Experimental validation plan

## Measurement definitions

For matched times, Cartesian position error is `e_p = p_measured - p_reference`; trajectory RMSE is `sqrt(mean(||e_p||²))`. State whether `p_measured` comes from encoder-based forward kinematics or independent external measurement. Encoder-derived position cannot independently verify unmodeled link deflection or calibration error.

Define the payload event timestamp, recovery error threshold, dwell interval, and allowed transient before testing. Recovery time is the first time after the event that the error enters and remains inside that predefined band for the stated dwell interval. A single threshold crossing is insufficient. The proposal's target is ≤0.5 s.

## Test matrix

| Test | Conditions | Record / compare |
| --- | --- | --- |
| Geometry and sensing | Static known poses and repeated readings | Dimensions, zero offsets, resolution, calibrated error |
| One-joint timing | Reviewed bench limits, sensor/drive/logging active | Period, execution time, jitter, deadlines |
| Nominal tracking | Declared trajectory, speed, and 100 g payload | RMSE, peak error, RMS/peak current |
| Sudden payload change | Controlled release/removal procedure, clear test area | Event time, recovery, current peak, adaptive parameters |
| Gradual payload change | Reproducible ramp or staged changes | Tracking/parameter/current trends |
| Baseline versus MRAC | Same trajectory, payload procedure, limits and sample rules | Paired metrics and repeated runs |
| Interaction | Defined controller structure and measurement method | Displacement, current, stability observations; force only when calibrated |
| Fault handling | Reviewed low-energy fault cases | Sensor timeout, limit response, stop action and recovery state |

## Reproducibility

Archive geometry, mass/payload, firmware/model version, sample rate, reference trajectory, gains, parameter bounds, encoder/current calibration, limit settings, initial conditions, and raw synchronized logs. Use repeat trials and report variability and unsuccessful runs. Freeze controller-selection rules before the final comparison.

## Numerical tests supplied now

The starter Python tests check known ideal poses, reachable/infeasible inverse solutions, axis ambiguity, and the analytic Jacobian against finite differences. They do not establish MRAC stability, hardware timing, physical safety, or the 5 mm/0.5 s targets.

## Public evidence package when experiments exist

Add a public-safe prototype photo, a short controlled demo, a reference-versus-measured path plot, error/current/parameter time plots, a metric table with trial counts, and scripts/configuration sufficient to regenerate the plots. Label CAD as CAD, simulation as simulation, and hardware data as measured.
