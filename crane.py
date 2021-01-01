from robot import Pid, Robot,LineEdge, LineSensor
from pybricks.parameters import Stop

def run(robot: Robot):
    robot.reset_sensors()
    
    # Initialize PID
    drive_pid = Pid(2, 0, 0)
    lf_pid = Pid(1.1, 0, 20)
    turn_pid= Pid(5, 0, 200)
    turn_pid2= Pid(3, 0, 15)
    
    
    # Drives foward to crane
    robot.drive(drive_pid, 1000, 0, 1200)
    robot.follow_line(lf_pid, 100, 1000, LineSensor.LEFT, LineEdge.LEFT)
    robot.stop_on_white(drive_pid, 100, 0, LineSensor.LEFT, 80)
    
    # Turns and drives toward the tree
    robot.turn(turn_pid2, 90)
    robot.follow_line(lf_pid, 100, 1200, LineSensor.LEFT, LineEdge.LEFT)
    robot.drive(drive_pid, 200, 90, 650)
    robot.stop_on_white(drive_pid, 200, 90, LineSensor.LEFT)

    # Drives forward, drops off the bat, and turns away
    robot.drive(drive_pid, -100, 90, 500)
    robot.turn(turn_pid, 45)
    robot.align(200)
    robot.drive(drive_pid, 100, 45, 300)
    robot.turn(turn_pid2, 135)
    robot.drive(drive_pid, -100, 135, 600)
    robot.turn(turn_pid, 165)

    # Hangs the drone and goes toward tree's bottom branch
    robot.move_yeeter(800, -205, False)  
    robot.drive(drive_pid, -100, 135, 250)
    robot.turn(turn_pid, -180)
    robot.drive(drive_pid, 100, -180, 800)
    robot.turn(turn_pid, -165)
    robot.run_yeeter(800, 800)
    robot.turn(turn_pid, -175)  
    robot.drive(drive_pid, -100, -165, 700)
    robot.turn(turn_pid, -146)
    robot.move_yeeter(800, -40)  
    robot.turn(turn_pid, -165)
    robot.move_yeeter(800, 20, False)  
    robot.drive(drive_pid, 200, -165, 1350)

    # Drops bottom blocks at tree
    robot.turn(turn_pid, 45)
    robot.drive(drive_pid, 300, 45, 400)
    robot.align(200)
    robot.drive(drive_pid, 100, 45, 600)
    robot.run_linear(500, 1500)
    
    # Slightly backs away
    robot.drive(drive_pid, -200, 45, 850)
    robot.run_linear(-500, 1500, False)
    robot.turn(turn_pid, 0)
    robot.stop_on_white(drive_pid, 200, 0, LineSensor.RIGHT)
    robot.turn(turn_pid, 93)
    
    # Moves and drops the block at crane 
    robot.run_yeeter(-300, 1200)
    robot.turn(turn_pid, 65)
    robot.move_yeeter(400, -8, False)
    robot.drive(drive_pid, -100, 75, 600)
    robot.turn(turn_pid, 87)
    robot.pulse_yeeter(350, 4)

    # Go back to base :)
    robot.run_yeeter(400, 700, False)
    robot.drive(drive_pid, -300, 65, 2200)
    robot.drive(drive_pid, -300, 0, 670)