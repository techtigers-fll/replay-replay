from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.parameters import Stop

def run(robot: Robot):
    robot.reset_sensors(-30)
    # Initialize PID

    drive_pid = Pid(5, 0, 10)
    turn_pid= Pid(3, 0, 15)
    # lf_pid = Pid(2,0.05, 20)
    lf_pid = Pid(1.1,0, 10)
    
    # robot.run_linear(800, 900)
    
    robot.follow_line(lf_pid, 100, 1300, LineSensor.LEFT, LineEdge.RIGHT)
    # robot.drive(drive_pid, 100, -30, 1000)
    # robot.run_yeeter(-400, 500)
    # robot.drive(drive_pid, -100, -35, 2000)
    # robot.follow_line(lf_pid, 100, 1000, LineSensor.LEFT, LineEdge.LEFT)
    # robot.stop_on_white(drive_pid, 50, -30, LineSensor.LEFT)
    # robot.drive(drive_pid, 100, -30, 400)
    # robot.turn(turn_pid, -90)
    # robot.drive(drive_pid, -100, -90, 4000)