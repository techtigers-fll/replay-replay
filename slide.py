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
    brick = EV3Brick()

    # robot.dropper_attachment_motor.run_until_stalled(100, Stop.BRAKE, 40)
    # robot.move_dropper(-100, 150)

#     while len(brick.buttons.pressed()) == 0:
#         wait(10)

#     while len(brick.buttons.pressed()) > 0:
#         wait(10)

    robot.drive(sharp_drive_pid, 400, 0, 450)
    robot.turn(turn_pid, -35)
    robot.drive(drive_pid, 400, -35, 2500)

    robot.drive(drive_pid, -100, -35, 1600)
    wait(500)
    robot.stop_motors()

    robot.drive(drive_pid, -200, -35, 1200)
    robot.drive(sharp_drive_pid, -400, 0, 1500)

    # robot.linear_attachment_motor.run_until_stalled(200, Stop.BRAKE, 20)
