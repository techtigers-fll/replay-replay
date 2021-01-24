from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,
                                GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Color,
                               SoundFile, Button)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font

def run(robot: Robot):
    robot.reset_sensors()

    while True:
        brick_buttons = brick.buttons.pressed()

        if Button.UP in brick_buttons:
            while True:
                if len(brick_buttons) == 0:
                    break
            robot.move_linear(-300, 1)

        if Button.DOWN in brick_buttons:
            while True:
                if len(brick_buttons) == 0:
                    break
            robot.move_linear(-300, 1)

