from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import Stop

def run(robot: Robot):
    robot.reset_sensors()
    
    # Initialize PID

    fast_drive_pid = Pid(5, 0.5, 10)
    slow_drive_pid = Pid(2, 0, 1)
    turn_pid= Pid(3, 0, 15)
    lf_pid = Pid(1, 0, 200)
    
    # Go up to black line

    robot.drive(fast_drive_pid, 200, 0, 2552) # was 1700 duration and 300 speed
    
    # Line follow to traffic jam

    robot.follow_line(lf_pid, 200, 1800, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.turn(turn_pid, -90)
    robot.drive(slow_drive_pid, 100, -90, 550)
    robot.drive(slow_drive_pid, -80, -90, 650)
    # Lift traffic jam up

    robot.move_yeeter(120, 35)
    robot.drive(fast_drive_pid, -100, -90, 1350)
    robot.move_yeeter(600, 180)
    robot.drive(slow_drive_pid, -100, -90, 200)
    
    # Go to Mitch Trubisky
    robot.drive(slow_drive_pid, 100, -90, 1300)
    robot.turn(turn_pid, 0)
    robot.follow_line(lf_pid, 200, 750, LineSensor.RIGHT, LineEdge.LEFT)
    robot.drive(fast_drive_pid, 200, 0, 1500)
    robot.follow_line(lf_pid, 200, 2500, LineSensor.RIGHT, LineEdge.LEFT)

    # Swing it
    robot.move_linear(600, 360)
    robot.drive(slow_drive_pid, 100, 0, 1000)
    robot.move_linear(-600, 360)

    # Go to and do elevator
    robot.drive(slow_drive_pid, -100, 0, 3100)
    robot.turn(turn_pid, -120, 1)
    robot.follow_line(lf_pid, 100, 2100, LineSensor.LEFT, LineEdge.RIGHT)
    robot.turn(turn_pid, -25, 1)
    robot.follow_line(lf_pid, 100, 3700, LineSensor.LEFT, LineEdge.RIGHT)
    robot.drive(slow_drive_pid, 100, -30, 1750)
    robot.move_yeeter(-100, 25)

    # go to and do safety factor ( 2 legs)
    robot.drive(slow_drive_pid, -100, -30, 400)
    robot.turn(turn_pid, -90, 1)
    robot.drive(slow_drive_pid, -100, -90, 2200)
    robot.move_linear(600, 360)
    robot.drive(fast_drive_pid, -100, -90, 1300)
    robot.drive(fast_drive_pid, 100, -90, 350)
    robot.turn(turn_pid, -120, 1)
    robot.move_linear(-600, 360)

    # Back out and go up ramp

    robot.drive(fast_drive_pid, 200, -120, 1300)
    robot.turn(turn_pid, 150, 1) 
    robot.follow_line(lf_pid, 100, 2800, LineSensor.RIGHT, LineEdge.LEFT)
    robot.drive(fast_drive_pid, 100, 150, 800)
    robot.turn(turn_pid, -120, 1)
    robot.follow_line(lf_pid, 100, 2500, LineSensor.LEFT, LineEdge.RIGHT) 
    robot.drive_base.drive_time(300, 0, 3000)

    # Delete This
    robot.move_yeeter(-600, 190)