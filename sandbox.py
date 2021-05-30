from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Button, Stop
import basketball, bench, slide, step_counter

def button_press():
    brick = EV3Brick()
    while len(brick.buttons.pressed()) == 0:
        wait(10)

    while len(brick.buttons.pressed()) > 0:
        wait(10)

def run(robot: Robot):
    robot.dropper_attachment_motor.run_until_stalled(100, Stop.BRAKE, 40)
    robot.move_dropper(-200, 150)

    ##210 angle

    button_press()

    basketball.run(robot)

    button_press()
    
    bench.run(robot)

    button_press()

    slide.run(robot)

    button_press()

    step_counter.run(robot)
