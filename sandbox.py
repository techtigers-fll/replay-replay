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

    robot.linear_attachment_motor.run_until_stalled(200, Stop.BRAKE, 20)
    # robot.drive(drive_pid, 400, 3, 3700)

    robot.stop_on_white(drive_pid, -100, 0, LineSensor.CENTER)
    robot.drive(drive_pid, -100, 0, 800)
    robot.turn(turn_pid, -35)
    robot.move_linear(-800, 1.6, False)
    robot.drive(drive_pid, 200, -35, 1500)

    robot.drive(drive_pid, 150, -35, 900)
    robot.drive(drive_pid, -150, -35, 275)
    robot.move_linear(200, 0.88)
    robot.drive(drive_pid, -150, -35, 200)
    robot.move_linear(400, 0.3, False)
    robot.drive(drive_pid, -150, -35, 1300)
    robot.drive(drive_pid, 400, -35, 500)
    # robot.move_linear(-800, 0.5, False)
    # robot.drive(drive_pid, -150, -35, 1300)
    # robot.drive(drive_pid, 400, -35, 500)
    
    return

    robot.stop_on_white(drive_pid, -100, -35, LineSensor.RIGHT)
    robot.drive(drive_pid, 100, -35, 300)
    robot.turn(turn_pid, 0)
    robot.follow_line(straight_line_follow_pid, 200, 2000, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.turn(turn_pid, 0)
    robot.align(100, LineSensor.LEFT, LineSensor.CENTER)

    robot.drive(drive_pid, 150, 0, 2000)
    robot.right_motor.run_time(800, 4000, Stop.BRAKE)

    robot.drive(drive_pid, -200, 0, 500)
    robot.stop_on_white(drive_pid, -50, 0, LineSensor.LEFT)
    robot.turn(turn_pid, -90) 
    robot.drive(drive_pid, -200, -90, 1200)
    robot.reset_sensors(-90)

    robot.drive(drive_pid, 400, -90, 1200)

    robot.move_linear(-800, 0.8)
    robot.turn(slow_turn_pid, 20)
    robot.drive(drive_pid, 200, 20, 300)
    robot.move_linear(800, 0.5)
    robot.drive(sharp_drive_pid, -100, 20, 1300)
    robot.move_linear(-800, 0.5)

