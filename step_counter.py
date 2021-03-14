from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,
                                GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Color,
                               SoundFile, Button)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font
import mario_music

def run(robot: Robot):
    straight_line_follow_pid = Pid(1.5, 0, 10)
    sharp_line_follow_pid = Pid(5, 0, 0)
    turn_pid = Pid(10, 0, 5)
    slow_turn_pid = Pid(3, 0, 0)
    drive_pid = Pid(1, 0, 0)
    sharp_drive_pid = Pid(4, 0, 0)
    robot.reset_sensors()
    

    # Going to step counter
    robot.linear_attachment_motor.run_until_stalled(200, Stop.BRAKE, 20)
    robot.drive(drive_pid, 400, 3, 2750)
    wait(500)
    robot.drive(drive_pid, 200, 3, 1000)

    # Backing out and squaring on wall
    robot.stop_on_white(sharp_drive_pid, -100, 10, LineSensor.CENTER)
    # robot.drive(drive_pid, -200, 10, 100)
    robot.turn(turn_pid, -90)
    robot.drive(drive_pid, -200, -90, 800)
    robot.left_motor.run_time(-800, 500)
    robot.reset_sensors(-90)

    # Doing pullup bar
    robot.drive(drive_pid, 400, -90, 700)
    robot.follow_line(straight_line_follow_pid, 200, 1000, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.drive(sharp_drive_pid, 400, -90, 350)
    robot.stop_on_black(drive_pid, 200, -90, LineSensor.LEFT)
    robot.drive(drive_pid, 200, -90, 250)
    robot.drive(drive_pid, -400, -90, 1400)
    robot.stop_on_black(drive_pid, -200, -90, LineSensor.RIGHT)

    # Turning to blue tire
    robot.drive(drive_pid, 200, -90, 400)
    robot.turn(slow_turn_pid, -30)

    # Doing blue tire
    robot.move_linear(-800, 1.4, False)
    robot.drive(drive_pid, 200, -30, 800)
    robot.drive(drive_pid, 150, -35, 900)
    robot.drive(drive_pid, -150, -35, 370)

    robot.move_linear(200, 0.64)
    robot.drive(drive_pid, -150, -35, 200)
    robot.move_linear(400, 0.3, False)
    robot.drive(drive_pid, -150, -35, 1300)
    robot.drive(drive_pid, 400, -35, 500)
    robot.drive(drive_pid, -400, -35, 300)

    # Going to treadmill
    robot.stop_on_white(drive_pid, -100, -35, LineSensor.RIGHT)
    robot.drive(drive_pid, 100, -35, 300)
    robot.turn(turn_pid, 0)
    robot.follow_line(straight_line_follow_pid, 200, 2000, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.stop_on_black(sharp_drive_pid, 200, 0, LineSensor.LEFT)
    robot.turn(turn_pid, 2)

    # Treadmill mission
    robot.drive(drive_pid, 300, 2, 1000)
    robot.right_motor.run_time(800, 3000, Stop.BRAKE)

    # Backing into wall
    robot.drive(drive_pid,-200, 0, 1000)
    robot.stop_on_black(drive_pid, -50, 0, LineSensor.LEFT)
    robot.turn(turn_pid, -90) 
    robot.drive(drive_pid, -400, -90, 600)
    robot.reset_sensors(-90)

    # Doing row machine
    robot.drive(drive_pid, 400, -90, 1000) # 1200 for full run

    robot.move_linear(-800, 0.7, False)
    robot.turn(slow_turn_pid, 10)
    robot.drive(drive_pid, 200, 10, 300)
    robot.move_linear(800, 0.7)
    robot.drive(sharp_drive_pid, -100, 10, 1300)
    robot.move_linear(-800, 0.5)
    robot.drive(drive_pid, -200, 10, 50)
    
    # Doing weight machine
    robot.move_linear(-600, 5.8, False)
    robot.turn(slow_turn_pid, -90)
    robot.drive(drive_pid, 400, -90, 1450)
    robot.drive(drive_pid, 200, -90, 1200)
    robot.reset_sensors(-90)
    robot.drive(drive_pid, -200, -90, 500)
    robot.turn(slow_turn_pid, 0)
    robot.drive(drive_pid, 200, 0, 150)
    robot.linear_attachment_motor.run_until_stalled(-200, Stop.BRAKE, 20)
    robot.move_linear(600, 5)
    robot.drive(drive_pid, -400, 0, 300)
    robot.drive(drive_pid, 400, 0, 800)
    
    # Going to black tire
    wait(100)
    # robot.move_linear(-800, 0.7)
    robot.drive(sharp_drive_pid, -400, 0, 375) # 300 when set up from weight machine, otherwise 375
    robot.turn(slow_turn_pid, 90)
    robot.drive(sharp_drive_pid, 400, 90, 400)
    robot.follow_line(straight_line_follow_pid, 100, 700, LineSensor.RIGHT, LineEdge.LEFT)
    robot.stop_on_white(drive_pid, 150, 90, LineSensor.LEFT)
    robot.move_linear(-600, 0.5, False)
    robot.turn(slow_turn_pid, 125)

    # Doing black tire
    robot.drive(drive_pid, 200, 125, 900)

    robot.drive(drive_pid, -200, 125, 300)
    robot.move_linear(400, 0.85)
    robot.drive(drive_pid, -400, 125, 600)
    robot.turn(turn_pid, 110)
    robot.drive(drive_pid, 200, 110, 1500)
    robot.move_dropper(100, 40)

    # Going to dance
    robot.drive(drive_pid, -200, 110, 600)
    robot.stop_on_white(drive_pid, -150, 110, LineSensor.LEFT)
    robot.drive(drive_pid, 200, 110, 300)
    robot.turn(turn_pid, 180)
    robot.drive(drive_pid, 400, 180, 1000)

    robot.turn(turn_pid, -130)
    robot.drive(drive_pid, 400, -130, 900)
    mario_music.run(robot)


