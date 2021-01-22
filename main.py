#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.tools import wait, StopWatch

from robot import Robot
import sandbox
import black
brick = EV3Brick()
robot = None
# while True:
#     # Create a new robot instance
robot = Robot()

#     # Check if robot is ok
#     if robot.is_ok():
#         # Robot is ok, check drift
#         if not robot.drift_check():
robot.beep()
#             break

#     # Robot not ok, wait for user to fix
#     robot.beep(True)

#     # Wait for button to be pressed and released
#     while not any(brick.buttons.pressed()):
#         wait(10)

#     while any(brick.buttons.pressed()):
#         wait(10)

# Initialize mission
mission = None
display_counter = 0
while True:
    if display_counter == 0:
        robot.display_sensor_values()
    display_counter = (display_counter + 1) % 500

    brick_buttons = brick.buttons.pressed()


    if Button.CENTER in brick_buttons:
        # Set mission selected to the sandbox program
        mission = sandbox

    if Button.UP in brick_buttons:
        # Set mission selected to the sandbox program
        mission = black

    # Check when no buttons are pressed
    if len(brick_buttons) == 0:
        # Run a mission if it is selected
        if not (mission is None):
            mission.run(robot)
            mission = None


    # Wait for a little bit before looping again
    wait(1)
