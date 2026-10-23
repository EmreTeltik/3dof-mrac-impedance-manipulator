# Embedded control development area

No robot-control firmware is included yet. The STM32H7-class platform, timer-driven loop, encoder/current acquisition, driver commands, limits, controller modes, and decimated logging are planned.

Before adding firmware, record the exact board/MCU, reviewed power/pin map, driver interface, toolchain/HAL versions, build/flash steps and a low-energy bench-test procedure. Keep target/sample-rate configuration separate from measured timing evidence. Test sensing and limits on one joint before full manipulator integration.
