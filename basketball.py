from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.tools import wait
from pybricks.parameters import Button
from pybricks.hubs import EV3Brick
from pybricks.parameters import Stop

brick = EV3Brick()
def run(robot: Robot):
    straight_line_follow_pid = Pid(1, 0, 5)
    straight_line_follow_pid2 = Pid(0.5, 0, 10)
    sharp_line_follow_pid = Pid(5, 0, 0)
    turn_pid = Pid(10, 0, 5)
    slow_turn_pid = Pid(3, 0, 0)
    drive_pid = Pid(1, 0, 0)
    robot.reset_sensors(0)

   #Drive out of base and stop on black line 
    robot.drive(drive_pid, 400, 0, 450) 
    robot.turn(turn_pid, 55)
    robot.stop_on_black(drive_pid, 300, 55, LineSensor.RIGHT)
    #Turn and follow line towards basketball
    robot.drive(drive_pid, -200, 55, 250)
    robot.turn(turn_pid, 0)
    robot.follow_line(straight_line_follow_pid, 200, 1700, LineSensor.RIGHT, LineEdge.LEFT)
    #Push ball into basket
    robot.drive(drive_pid, 100, 0, 2000)

    #Lift Boccia share and basketball all the way up
    robot.move_linear(-800, 6.3)
    robot.move_linear(800, 6.1)
    robot.move_linear(-800, 6.4)
    robot.move_linear(800, 0.5)
    robot.move_linear(800, 4.5, False)


    #Back out and go towards aim and frame
    robot.drive(drive_pid, -400, 0, 250)
    robot.turn(slow_turn_pid, 90)
    robot.move_dropper(-200, 60, False)
    robot.drive(drive_pid, 400, 90, 1000)
    robot.follow_line(straight_line_follow_pid, 
            200, 500, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.turn(turn_pid, 90)
    robot.drive(drive_pid, 200, 90, 500)
    #Align, push, and drop aim and frame
    robot.stop_on_black(drive_pid, 200, 90 , LineSensor.LEFT)
    robot.align(200, LineSensor.LEFT, LineSensor.CENTER)
    robot.turn(turn_pid, 60)
    robot.drive(drive_pid, 100, 60, 1000)
    robot.drive(drive_pid, -100, 60, 100)
    robot.move_linear(-800, 2.5)
    robot.move_linear(800,0.5)
    # robot.move_linear(800, 3.5, False)
    #Back out and drop the blocks into the target area
    robot.stop_on_black(drive_pid, -100, 60, LineSensor.CENTER)
    robot.turn(turn_pid, 0)
    robot.drive(drive_pid, 200, 0, 700)
    robot.move_dropper(-400, 200)
    
    
    wait(500)
    #Reset dropper to and collect health unit 
    robot.move_dropper(200, 200, False)
    robot.drive(drive_pid, -100, 0, 300)
    robot.stop_on_black(drive_pid, -200, 0, LineSensor.CENTER) 
    robot.move_linear(800, 3.5, False)
    robot.drive(drive_pid, 200, 0, 300)
    robot.turn(turn_pid, -45)

    robot.drive(drive_pid, 200, -45, 1700)
    robot.turn(turn_pid, -135)
    robot.drive(drive_pid, 200, -135, 1000)
    robot.stop_on_black(drive_pid, 200, -135, LineSensor.CENTER) 
    robot.drive(drive_pid, 200, -135, 100)
    robot.turn(turn_pid, -75)
    robot.drive(drive_pid, 200, -75, 500)
    robot.follow_line(straight_line_follow_pid,
            400, 1000, LineSensor.CENTER, LineEdge.RIGHT)
    robot.drive(drive_pid, 200, -75, 2000)
    robot.move_dropper(200, 5, False)
    robot.move_linear(-800, 4.5)
    
    

