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

    robot.drive(drive_pid, 400, 0, 3500)

    robot.stop_on_white(drive_pid, -100, 0, LineSensor.CENTER)
    robot.turn(turn_pid, -40)
    robot.move_linear(-800, 1.2, False)
    robot.drive(drive_pid, 200, -40, 1000)

    robot.drive(drive_pid, 150, -40, 1000)
    robot.move_linear(400, 0.95, False)
    wait(200)
    robot.drive(drive_pid, -150, -40, 1500)
    robot.drive(drive_pid, 400, -40, 500)
    robot.drive(drive_pid, -400, -40, 350)
    robot.turn(turn_pid, 0)
    robot.follow_line(straight_line_follow_pid, 200, 2000, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.drive_dead_reckon(800, 1500)
    robot.right_motor.run_time(800, 3000, Stop.BRAKE)
    robot.drive_dead_reckon(-800, 1500)

    # robot.drive_dead_reckon(200, 2000)
    # robot.right_motor.run_time(800, 3000, Stop.BRAKE)
