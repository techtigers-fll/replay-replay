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
    drive_pid = Pid(2, 0, 0)
    sharp_drive_pid = Pid(4, 0, 0)
    robot.reset_sensors()
#TESTING CUZ NOT WORKING

    
    #robot.drive(drive_pid, 50, 0, 3000)
    #robot.drive(drive_pid, -50, 0, 3000)
    
    robot.drive(drive_pid, 400, 0, 2500)

    robot.drive(drive_pid, -100, 0, 1400)
    wait(500)
    robot.stop_motors()

    robot.drive(drive_pid, -200, -3, 1200)
    robot.drive(sharp_drive_pid, -400, 30, 1500)
    return
    robot.turn(turn_pid, -90)
    robot.drive(drive_pid, 200, -90, 500)

    robot.move_linear(-800, 1)

    robot.stop_motors()

