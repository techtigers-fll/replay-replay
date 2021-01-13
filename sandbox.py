from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,
                                GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Color,
                               SoundFile, Button)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font

def run1(robot: Robot):
    line_follow_pid = Pid(2, 0, 0)
    drive_pid = Pid(2, 0, 0)
    turn_pid = Pid(5, 0, 0)
    robot.reset_sensors()
    brick = EV3Brick()

    def wait_button_press():
        while not any(brick.buttons.pressed()):
            wait(10)
        while any(brick.buttons.pressed()):
            wait(10)
        return

    robot.turn(turn_pid, 0)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 0)
    wait(1000)
    robot.turn(turn_pid, -30)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 0)
    wait(1000)
    robot.turn(turn_pid, -45)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 0)
    wait(1000)
    robot.turn(turn_pid, -60)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 0)
    wait(1000)
    robot.turn(turn_pid, -90)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 0)
    wait(1000)
    robot.turn(turn_pid, 30)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 0)
    wait(1000)
    robot.turn(turn_pid, 45)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 0)
    wait(1000)
    robot.turn(turn_pid, 60)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 0)
    wait(1000)
    robot.turn(turn_pid, 90)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 30)
    wait(1000)
    robot.turn(turn_pid, 0)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 30)
    wait(1000)
    robot.turn(turn_pid, 45)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 30)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 45)
    wait(1000)
    robot.turn(turn_pid, 60)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 45)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 60)
    wait(1000)
    robot.turn(turn_pid, 90)
    print(robot.gyro.angle())
    wait_button_press()

    robot.turn(turn_pid, 60)
    print(robot.gyro.angle())
    wait_button_press()

def run(robot: Robot):
        linear_attachment_motor = Motor(Port.C)
        linear_attachment_motor.run_time(-1000, 3000, Stop.BRAKE)
        linear_attachment_motor.run_time(1000, 3000, Stop.BRAKE)
