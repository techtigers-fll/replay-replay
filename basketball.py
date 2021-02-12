from robot import Pid, Robot, LineEdge, LineSensor

def run(robot: Robot):
    straight_line_follow_pid = Pid(1, 0, 5)
    sharp_line_follow_pid = Pid(5, 0, 0)
    turn_pid = Pid(10, 0, 5)
    slow_turn_pid = Pid(3, 0, 0)
    drive_pid = Pid(1, 0, 0)
    robot.reset_sensors()

    robot.drive(drive_pid, 400, 0, 450) 
    robot.turn(turn_pid, 55)
    robot.drive(drive_pid, 400, 55, 700) 
    robot.stop_on_black(drive_pid, 100, 55, LineSensor.RIGHT)
    robot.drive(drive_pid, -50, 55, 200)
    robot.turn(turn_pid, 0)
    # robot.follow_line(straight_line_follow_pid, 400, 1600, LineSensor.RIGHT, LineEdge.RIGHT)
    robot.drive(drive_pid, 400, 0, 1600)

    robot.move_linear(-800, 6.15)
    robot.move_linear(800, 5.1)
    robot.move_linear(-800, 5.1)
    robot.move_linear(800, 0.5)
    robot.move_linear(800, 5.65, False)
    robot.drive(drive_pid, -400, 0, 600)
