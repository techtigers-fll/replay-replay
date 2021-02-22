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
    straight_line_follow_pid = Pid(1.5, 0, 10)
    sharp_line_follow_pid = Pid(5, 0, 0)
    turn_pid = Pid(10, 0, 5)
    slow_turn_pid = Pid(3, 0, 0)
    drive_pid = Pid(2, 0, 0)
    sharp_drive_pid = Pid(4, 0, 0)
    robot.reset_sensors()

    robot.linear_attachment_motor.run_until_stalled(200, Stop.BRAKE, 20)
    robot.drive(drive_pid, 400, 3, 3700)

    robot.stop_on_white(sharp_drive_pid, -100, 10, LineSensor.CENTER)
    robot.drive(drive_pid, 200, 0, 100)
    robot.turn(turn_pid, -90)
    robot.drive(drive_pid, -200, 0, 800)
    robot.left_motor.run_time(-800, 500)
    robot.reset_sensors(-90)
    robot.drive(drive_pid, 800, -90, 700)
    robot.follow_line(straight_line_follow_pid, 200, 1000, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.drive(sharp_drive_pid, 800, -90, 450)
    robot.stop_on_black(drive_pid, 200, -90, LineSensor.LEFT)
    robot.drive(drive_pid, 200, -90, 250)
    robot.drive(drive_pid, -800, -90, 1400)
    robot.stop_on_black(drive_pid, -200, -90, LineSensor.RIGHT)

    robot.drive(drive_pid, 200, -90, 400)
    robot.turn(slow_turn_pid, -30)

    robot.move_linear(-800, 1.3, False)
    robot.drive(drive_pid, 200, -30, 800)

    robot.drive(drive_pid, 150, -35, 900)
    robot.drive(drive_pid, -150, -35, 275)

    robot.move_linear(200, 0.68)
    robot.drive(drive_pid, -150, -35, 200)
    robot.move_linear(400, 0.3, False)
    robot.drive(drive_pid, -150, -35, 1300)
    robot.drive(drive_pid, 400, -35, 500)
    robot.drive(drive_pid, -400, -35, 300)

def run(robot: Robot):
    straight_line_follow_pid = Pid(1.5, 0, 10)
    sharp_line_follow_pid = Pid(5, 0, 0)
    turn_pid = Pid(10, 0, 5)
    slow_turn_pid = Pid(3, 0, 0)
    drive_pid = Pid(1, 0, 0)
    sharp_drive_pid = Pid(4, 0, 0)
    robot.reset_sensors()

    robot.linear_attachment_motor.run_until_stalled(200, Stop.BRAKE, 20)
    robot.drive(drive_pid, 400, 3, 3700)

    robot.stop_on_white(sharp_drive_pid, -100, 10, LineSensor.CENTER)
    robot.drive(drive_pid, 200, 0, 100)
    robot.turn(turn_pid, -90)
    robot.drive(drive_pid, -200, 0, 800)
    robot.left_motor.run_time(-800, 500)
    robot.reset_sensors(-90)

    robot.drive(drive_pid, 800, -90, 700)
    robot.follow_line(straight_line_follow_pid, 200, 1000, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.drive(sharp_drive_pid, 800, -90, 450)
    robot.stop_on_black(drive_pid, 200, -90, LineSensor.LEFT)
    robot.drive(drive_pid, 200, -90, 250)
    robot.drive(drive_pid, -800, -90, 1400)
    robot.stop_on_black(drive_pid, -200, -90, LineSensor.RIGHT)

    robot.drive(drive_pid, 200, -90, 400)
    robot.turn(slow_turn_pid, -30)

    robot.move_linear(-800, 1.3, False)
    robot.drive(drive_pid, 200, -30, 800)
    robot.drive(drive_pid, 150, -35, 900)
    robot.drive(drive_pid, -150, -35, 275)

    robot.move_linear(200, 0.68)
    robot.drive(drive_pid, -150, -35, 200)
    robot.move_linear(400, 0.3, False)
    robot.drive(drive_pid, -150, -35, 1300)
    robot.drive(drive_pid, 400, -35, 500)
    robot.drive(drive_pid, -400, -35, 300)

    robot.stop_on_white(drive_pid, -100, -35, LineSensor.RIGHT)
    robot.drive(drive_pid, 100, -35, 300)
    robot.turn(turn_pid, 0)
    robot.follow_line(straight_line_follow_pid, 200, 2000, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.turn(turn_pid, 0)
    robot.align(100, LineSensor.LEFT, LineSensor.CENTER)

    robot.drive(drive_pid, 300, 0, 1000)
    robot.right_motor.run_time(800, 3500, Stop.BRAKE)

    robot.drive(drive_pid,-200, 0, 500)
    robot.stop_on_black(drive_pid, -50, 0, LineSensor.LEFT)
    robot.turn(turn_pid, -90) 
    robot.drive(drive_pid, -200, -90, 1200)
    robot.reset_sensors(-90)
    # robot.move_linear(-800, 0.7)


    robot.drive(drive_pid, 400, -90, 1000) # 1200 for full run

    robot.move_linear(-800, 0.5, False)
    robot.turn(slow_turn_pid, 20)
    robot.drive(drive_pid, 200, 20, 375)
    robot.move_linear(800, 0.5)
    robot.drive(sharp_drive_pid, -100, 20, 1300)
    robot.move_linear(-800, 0.5)
    robot.drive(drive_pid, -200, 20, 50)
    
    robot.move_linear(-600, 5.8, False)
    robot.turn(slow_turn_pid, -90)
    robot.drive(drive_pid, 200, -90, 500)
    robot.align(200, LineSensor.LEFT, LineSensor.CENTER)
    robot.drive(drive_pid, 400, -90, 700)
    robot.turn(slow_turn_pid, 0)
    robot.drive(drive_pid, 200, 0, 100)
    robot.linear_attachment_motor.run_until_stalled(-200, Stop.BRAKE, 20)
    robot.move_linear(600, 5)
    robot.drive(drive_pid, -400, 0, 300)
    robot.drive(drive_pid, 400, 0, 800)
    
    wait(1)
    robot.drive(drive_pid, -400, 0, 300)
    # robot.turn(slow_turn_pid, 90)

    # robot.move_linear(-600, 0.5, False)
    # robot.drive(drive_pid, 200, 110, 1800)

    # robot.drive(drive_pid, -200, 110, 300)
    # robot.move_linear(400, 0.9)
    # robot.drive(drive_pid, -200, 110, 1500)
    # robot.turn(slow_turn_pid, 100)
    # robot.drive(drive_pid, 200, 100, 1700)
    # robot.move_dropper(100, 45)
    # robot.move_linear(400, 1.15)
