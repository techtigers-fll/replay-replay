from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,
                                GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Color,
                               SoundFile, Button)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font

def run(robot: Robot):
    line_follow_pid = (2, 0, 0)
    robot.follow_line(line_follow_pid, 300, 10, LineSensor.CENTER, LineEdge.LEFT)
    # big_font = Font(size=18)
    # brick.screen.set_font(big_font)        
    # brick.screen.draw_text(0, 20, "Checking Gyro drift...")
