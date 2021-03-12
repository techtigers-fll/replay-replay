from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Button
import basketball, bench, slide, step_counter

def button_press():
    brick = EV3Brick()
    while len(brick.buttons.pressed()) == 0:
        wait(10)

    while len(brick.buttons.pressed()) > 0:
        wait(10)

def run(robot: Robot):
    basketball.run(robot)

    button_press()
    
    bench.run(robot)

    button_press()

    slide.run(robot)

    button_press()

    step_counter.run(robot)
