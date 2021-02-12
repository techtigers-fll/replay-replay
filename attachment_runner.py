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
    brick.screen.clear()
    running = True
    font = Font(size=14)
    brick.screen.set_font(font)
    while running:
        if Button.RIGHT in brick.buttons.pressed():
            while len(brick.buttons.pressed()) != 0: 
                pass
            brick.screen.clear()
            brick.screen.draw_text(0,20, "Switching to Block Dropper")
            attachment_motor_name = "block dropper"
            attachment_motor = robot.dropper_attachment_motor

        if Button.LEFT in brick.buttons.pressed():
            while len(brick.buttons.pressed()) != 0:
                pass
            brick.screen.clear()
            brick.screen.draw_text(0,20, "Switching to Linear Gear")
            attachment_motor_name = "linear gear"
            attachment_motor = robot.linear_attachment_motor

        if Button.UP in brick.buttons.pressed():
	    brick.screen.draw_text(0,20, "Moving " + attachment_motor_name + " up")
	    attachment_motor.run(-200)
            while len(brick.buttons.pressed()) != 0:
		pass
	    attachment_motor.stop()
            brick.screen.clear()

        if Button.DOWN in brick.buttons.pressed():
	    brick.screen.draw_text(0,20, "Moving " + attachment_motor_name + " down")
	    attachment_motor.run(200)
            while len(brick.buttons.pressed()) != 0:
		pass
	    attachment_motor.stop()
            brick.screen.clear()

        if Button.CENTER in brick.buttons.pressed():
            while len(brick.buttons.pressed()) != 0:
                pass
            running = False
        wait(1)
