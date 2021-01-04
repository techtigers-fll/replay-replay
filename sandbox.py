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
    line_follow_pid = Pid(2, 0, 0)
    drive_pid = Pid(2, 0, 0)
    turn_pid = Pid(5, 0, 0)
    robot.reset_sensors()

    # robot.drive(drive_pid, 300, 0, 5000)
    # robot.follow_line(line_follow_pid, 300, 5000, LineSensor.LEFT, LineEdge.LEFT)
    # robot.turn(turn_pid, 90)
    # robot.turn(turn_pid, -90)
    # robot.stop_on_white(drive_pid, 150, 0, LineSensor.CENTER)
    robot.align(300, LineSensor.LEFT, LineSensor.CENTER)
