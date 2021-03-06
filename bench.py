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
    robot.reset_sensors()

    brick = EV3Brick()
    brick_buttons = brick.buttons.pressed()

    robot.drive(drive_pid, 200, 0, 2000)
    robot.drive(drive_pid, 80, 0, 1000)
    robot.move_linear(800, 4.6, False)
    robot.drive(drive_pid, -200, 0, 1500)
    return
    while not any(brick.buttons.pressed()):
        wait(10)

    while any(brick.buttons.pressed()):
        wait(10)
    
#Slide code, run directly after bench
    robot.reset_sensors()

    robot.move_linear(800, 1)

    robot.drive(drive_pid, 200, 0, 300)
    robot.turn(turn_pid, 80)
    robot.drive(drive_pid, 200, 80, 1400)
    robot.follow_line(straight_line_follow_pid, 100, 1750, LineSensor.LEFT, LineEdge.LEFT)

    robot.turn(turn_pid, 60)
    robot.drive(drive_pid, 200, 60, 1400)

    robot.drive(drive_pid, -100, 60, 1400)
    wait(500)
    robot.drive(drive_pid, -200, 60, 1200)
    robot.turn(turn_pid, -90)
    robot.drive(drive_pid, 200, -90, 500)

    robot.move_linear(-800, 1)

    robot.stop_motors()
