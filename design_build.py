from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.parameters import Stop

def run(robot: Robot):
    robot.reset_sensors()

    
    # Initialize PID
    drive_pid = Pid(2, 0, 0)
    lf_pid = Pid(1.1, 0, 20)
    turn_pid= Pid(3, 0, 15)


    # Leave Home and head towards line
    # Robot needs to be backwards with att5achement in the back
    # Left wheel of the robot is 2 cubes away from home 
    # Go towards black circle

    robot.drive(drive_pid, -2000, 0, 100)
    robot.drive(drive_pid, 3000, 0, 50)
    robot.drive(drive_pid, -100, 0, 5050)
    
    # Leave M012/13 (Blocks) in circle and yeet attachment
    # 3 of each color (red, brown, white blocks)

    robot.drive(drive_pid, 200, 0, 400)
    robot.run_yeeter(600, 1000)
    robot.drive(drive_pid, 200, 0, 400)
    robot.drive(drive_pid, 200, -90, 800)
    robot.move_yeeter(-400, 142, False)
    robot.drive(drive_pid, -200, -90, 1800)