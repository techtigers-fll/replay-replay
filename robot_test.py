from pybricks import ev3brick as brick
from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import Stop

def run(robot: Robot):
    robot.reset_sensors()
    brick.sound.beep(1000, 500)
    if robot.right_gyro.angle()!=0:
        brick.clear()
        brick.display.text("Invalid right gyro value")

    if robot.left_gyro.angle()!=0:
        brick.clear()
        brick.display.text("Invalid left gyro value")

    wait(5000)

def test_gyro (expected_angle):

    left_gyro_value = robot.left_gyro.angle()
    right_gyro_value = robot.right_gyro.angle()

    if right_gyro_value != 0:
        brick.clear()
        brick.display.text("Invalid right gyro value")

    if robot.left_gyro.angle()!=0:
        brick.clear()
        brick.display.text("Invalid left gyro value")
