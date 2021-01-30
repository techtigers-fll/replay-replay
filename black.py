from robot import Pid, Robot, LineEdge, LineSensor

def run(robot: Robot):
    straight_line_follow_pid = Pid(1, 0, 0)
    sharp_line_follow_pid = Pid(5, 0, 0)
    turn_pid = Pid(10, 0, 5)
    slow_turn_pid = Pid(3, 0, 0)
    drive_pid = Pid(1, 0, 0)
    robot.reset_sensors()

    robot.drive(drive_pid, 400, 0, 375) 
    robot.turn(turn_pid, 55)
    robot.drive(drive_pid, 400, 55, 725) 
    robot.turn(turn_pid, 0)
    robot.follow_line(straight_line_follow_pid, 400, 1500, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.move_linear(-800, 6.15)
    robot.move_linear(800, 4.9)
    robot.move_linear(-800, 4.9)
    robot.move_linear(800, 0.5)
    robot.move_linear(800, 5.65, False)
    robot.drive(drive_pid, -400, 0, 600)
