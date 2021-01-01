#!/usr/bin/env pybricks-micropython
from pybricks.hubs import Ev3Brick
from pybricks.parameters import Button
from pybricks.tools import wait, print, StopWatch

from robot import Robot
import ida
import crane
import design_build
import robot_test
import sandbox
brick = Ev3Brick()
robot = None
while True:
    # Create a new robot instance
    robot = Robot()

    # Check if robot is ok
    if robot.is_ok():
        # Robot is ok, check drift
        if not robot.drift_check():
            robot.beep()
            break

    # Robot not ok, wait for user to fix
    robot.beep(True)

    # Wait for button to be pressed and released
    while not any(brick.buttons()):
        wait(10)

    while any(brick.buttons()):
        wait(10)

# Initialize mission
mission = None
display_counter = 0
while True:
    if display_counter == 0:
        robot.display_sensor_values()
    display_counter = (display_counter + 1) % 500

    brick_buttons = brick.buttons.pressed()

    # Check if down button is pressed
    if Button.DOWN in brick_buttons:
        # Set mission selected to ida
        mission = ida

    if Button.UP in brick_buttons:
        # Set mission selected to crane
        mission = crane

    if Button.RIGHT in brick_buttons:
        # Set mission selected to design and build
        mission = design_build

    if Button.LEFT in brick_buttons:
        # Set mission selected to the robot test program
        mission = robot_test

    if Button.CENTER in brick_buttons:
        # Set mission selected to the sandbox program
        mission = sandbox

    # Check when no buttons are pressed
    if len(brick_buttons) == 0:
        # Run a mission if it is selected
        if not (mission is None):
            mission.run(robot)
            mission = None


    # Wait for a little bit before looping again
    wait(1)
