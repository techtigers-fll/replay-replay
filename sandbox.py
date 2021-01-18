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
    line_follow_pid = Pid(1, 0, 0)
    turn_pid = Pid(10, 0, 5)
    drive_pid = Pid(1, 0, 0)
    robot.reset_sensors()

    # robot.follow_line(line_follow_pid, 200, 3000, LineSensor.RIGHT, LineEdge.RIGHT)
    # robot.move_linear(-2000, 11)
    # robot.move_linear(2000, 9)
    # robot.move_linear(-2000, 9)
    # robot.move_linear(2000, 1)
    # robot.move_linear(2000, 10, False)
    # robot.drive(drive_pid, -200, 0, 1000)
    robot.move_linear(-750, 5)
    robot.move_linear(750, 5)
