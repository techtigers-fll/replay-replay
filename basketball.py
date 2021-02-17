from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.tools import wait

def run(robot: Robot):
    straight_line_follow_pid = Pid(1, 0, 5)
    sharp_line_follow_pid = Pid(5, 0, 0)
    turn_pid = Pid(10, 0, 5)
    slow_turn_pid = Pid(3, 0, 0)
    drive_pid = Pid(1, 0, 0)
    robot.reset_sensors()

    robot.drive(drive_pid, 400, 0, 450) 
    robot.turn(turn_pid, 55)
    robot.drive(drive_pid, 400, 55, 900) 
    robot.stop_on_black(drive_pid, 100, 55, LineSensor.RIGHT)
    robot.drive(drive_pid, -50, 55, 200)
    robot.turn(turn_pid, 0)
    robot.drive(drive_pid, 400, 0, 1600)

    robot.move_linear(-800, 6.8)
    robot.move_linear(800, 6)
    robot.move_linear(-800, 6)
    robot.move_linear(800, 0.5)
    robot.move_linear(800, 4.65, False)

    robot.drive(drive_pid, -400, 0, 250)
    robot.turn(slow_turn_pid, 90)
    robot.drive(drive_pid, 400, 90, 1000)
    robot.follow_line(straight_line_follow_pid, 
            200, 1000, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.turn(turn_pid, 90)
    robot.align(200, LineSensor.LEFT, LineSensor.CENTER)
    robot.turn(turn_pid, 60)
    robot.drive(drive_pid, 100, 60, 1200)
    robot.drive(drive_pid, -100, 60, 300)
    robot.move_linear(-800, 2.5)
    robot.move_linear(800,0.5)
    robot.move_linear(800, 3.75, False)
    robot.stop_on_black(drive_pid, -100, 60, LineSensor.CENTER)
    robot.turn(turn_pid, 0)
    robot.drive(drive_pid, 200, 0, 800)
    robot.move_dropper(100, 45)
    
    wait(500)
    robot.drive(drive_pid, -200, -10, 1700)
    robot.align(100, LineSensor.LEFT, LineSensor.CENTER)
    robot.drive(drive_pid, -200, -10, 1600)
    robot.stop_on_black(drive_pid, 200, -10, LineSensor.CENTER)

    robot.drive(drive_pid, 200, 0, 400)
    robot.turn(turn_pid, -52)
    robot.drive(drive_pid, 200, -52, 1600) 
    robot.turn(slow_turn_pid, -135)
    robot.drive(drive_pid, 200, -135, 1600)
    robot.turn(slow_turn_pid, -110)
    robot.drive(drive_pid, 200, -110, 1100)
    robot.drive(drive_pid, -200,-110, 800)
    robot.turn(turn_pid, -60)
    robot.drive(drive_pid, 400, -60, 800)
    robot.drive(drive_pid, 200, -60, 1100)
    robot.turn(slow_turn_pid, -90)
    robot.drive(drive_pid, 200, -90, 1500)

     
