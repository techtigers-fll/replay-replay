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
    robot.reset_sensors()
    brick = EV3Brick()
    attachment_motor = 'linear gear'
    while True:
        brick_buttons = brick.buttons.pressed()
        if Button.UP in brick_buttons:
            while True:
                if len(brick_buttons) == 0:
                    break
            brick.scren.clear()
            brick.screen.draw_text(0,20, "Moving " + attachment_motor + " gear up")
            robot.move_linear(20, 1)

        if Button.DOWN in brick_buttons:
            while True:
                if len(brick_buttons) == 0:
                    break
            brick.screen.clear()
            brick.screen.draw_text(0,20, "Moving linear gear down")
            robot.move_linear(-20, 1)
        if Button.RIGHT in brick_buttons:
            while True: 
                if len(brick_buttons) == 0:
                    break
            brick.screen.clear()
            brick.screen.draw_text(0,20, "Switching to Block Dropper")
            if Button.UP in brick_buttons:
                while True:
                    if len(brick_buttons) == 0:
                        break
                brick.screen.clear()
                brick.screen.draw_text(0,20, "Moving Block Dropper")
            if Button.DOWN in brick_buttons:
                while True:
                    if len(brick_buttons) == 0:
                        break
                brick.screen.clear()
                brick.screen.draw_text(0,20, "Moving Block Dropper")


                


            


