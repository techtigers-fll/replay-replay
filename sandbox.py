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
    straight_line_follow_pid = Pid(1.5, 0, 10)
    sharp_line_follow_pid = Pid(5, 0, 0)
    turn_pid = Pid(10, 0, 5)
    slow_turn_pid = Pid(3, 0, 0)
    drive_pid = Pid(1, 0, 0)
    sharp_drive_pid = Pid(4, 0, 0)
    robot.reset_sensors()

    # robot.drive(drive_pid, 400, 0, 3500)
    robot.drive(sharp_drive_pid, -400, 30, 600)
    robot.turn(turn_pid, -32)
    robot.move_linear(-800, 2, False)
    robot.drive(drive_pid, 200, -32, 1675)
    robot.move_linear(800, 1.6)
    robot.drive(drive_pid, -200, -32, 1000)

    robot.move_linear(800, 0.3)
