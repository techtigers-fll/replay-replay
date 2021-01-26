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

    # robot.move_linear(800, 0.5)
    # robot.move_linear(800, 5.65, False)

    # robot.drive(drive_pid, -400, 0, 100)
    # robot.turn(slow_turn_pid, 90)
    # robot.drive(drive_pid, 400, 90, 1500)

    # robot.follow_line(straight_line_follow_pid, 200, 1400, LineSensor.RIGHT, LineEdge.LEFT)
    # robot.align(100, LineSensor.LEFT, LineSensor.CENTER)
    robot.turn(turn_pid, -20)
    robot.beep()
    robot.print_sensor_values()
    robot.drive(drive_pid, 100, -20, 1700)

    # robot.follow_line(straight_line_follow_pid, 200, 2500, LineSensor.RIGHT, LineEdge.RIGHT)
    # robot.drive(drive_pid, -200, 0, 500)
    # robot.turn(turn_pid, -15)
    # robot.drive(drive_pid, 200, 0, 300)
    # robot.move_linear(-800, 4.9)
    # robot.move_linear(800, 4.9)
    robot.stop_motors()
