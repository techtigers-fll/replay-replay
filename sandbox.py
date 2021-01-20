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
    straight_line_follow_pid = Pid(1, 0, 0)
    sharp_line_follow_pid = Pid(5, 0, 0)
    turn_pid = Pid(10, 0, 5)
    slow_turn_pid = Pid(3, 0, 0)
    drive_pid = Pid(1, 0, 0)
    robot.reset_sensors()

    robot.drive(drive_pid, 200, 0, 800) 
    robot.turn(slow_turn_pid, 55)
    robot.drive(drive_pid, 200, 55, 400) 
    robot.follow_line(straight_line_follow_pid, 200, 1000, LineSensor.RIGHT, LineEdge.LEFT)
    robot.turn(slow_turn_pid, 0)
    robot.follow_line(straight_line_follow_pid, 200, 3000, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.move_linear(-2000, 11)
    robot.move_linear(2000, 9)
    robot.move_linear(-2000, 9)
    robot.move_linear(2000, 1)
    robot.move_linear(2000, 10, False)
    robot.drive(drive_pid, -200, 0, 1000)
