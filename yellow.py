from robot import Pid, Robot, LineEdge, LineSensor

def run(robot: Robot):
    drive_pid = Pid(1, 0, 0)

    robot.reset_sensors()
    robot.drive(drive_pid, 170, 0, 2500)
    robot.drive(drive_pid, -1700, 0, 2500)
