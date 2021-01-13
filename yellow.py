from robot import Pid, Robot, LineEdge, LineSensor

def run(robot: Robot):
    angle = 5
    robot.move_linear(-1000, angle)
    robot.move_linear(1000, angle)
