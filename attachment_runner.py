from robot import Pid, Robot, LineEdge, LineSensor
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,
                                GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Color,
                               SoundFile, Button)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font

font = Font(size=14)
small_font = Font(size=8)
brick = EV3Brick()
def run(robot: Robot):
    robot.reset_sensors()
    brick.screen.clear()
    running = True
    speeds = [50, 100, 200, 400, 800]
    linear_counter = -1
    dropper_counter = -1
    display_menu()
    while running:
        brick.screen.set_font(font)
        if Button.RIGHT in brick.buttons.pressed():
            while len(brick.buttons.pressed()) != 0: 
                pass
            brick.screen.clear()
            attachment_motor_name = "block dropper"
            attachment_motor = robot.dropper_attachment_motor
            dropper_counter += 1
            linear_counter = -1
            speed = speeds[dropper_counter % len(speeds)]
            brick.screen.draw_text(0,0, "Switching to Block Dropper")
            brick.screen.draw_text(0,20, "Speed: " + str(speed))

        if Button.LEFT in brick.buttons.pressed():
            while len(brick.buttons.pressed()) != 0:
                pass
            brick.screen.clear()
            attachment_motor_name = "linear gear"
            attachment_motor = robot.linear_attachment_motor
            linear_counter += 1
            dropper_counter = -1
            speed = speeds[linear_counter % len(speeds)]
            brick.screen.draw_text(0,0, "Switching to Linear Gear")
            brick.screen.draw_text(0,20, "Speed: " + str(speed))

        if Button.UP in brick.buttons.pressed():
            brick.screen.clear()
	    brick.screen.draw_text(0,0, "Moving " + attachment_motor_name + " up")
            brick.screen.draw_text(0,20, "Speed: " + str(speed))
	    attachment_motor.run(-speed)
            while len(brick.buttons.pressed()) != 0:
		pass
	    attachment_motor.hold()
            brick.screen.clear()
            display_menu()

        if Button.DOWN in brick.buttons.pressed():
            brick.screen.clear()
	    brick.screen.draw_text(0,0, "Moving " + attachment_motor_name + " down")
            brick.screen.draw_text(0,20, "Speed: " + str(speed))
	    attachment_motor.run(speed)
            while len(brick.buttons.pressed()) != 0:
		pass
	    attachment_motor.hold()
            brick.screen.clear()
            display_menu()

        if Button.CENTER in brick.buttons.pressed():
            while len(brick.buttons.pressed()) != 0:
                pass
            running = False
        wait(1)

def display_menu():
    brick.screen.set_font(small_font)
    brick.screen.clear()
    brick.screen.draw_text(0,0, "Select a button: ")
    brick.screen.draw_text(0,20, "Right - set to block dropper and change speed")
    brick.screen.draw_text(0,40, "Left - set to linear gear and change speed")
    brick.screen.draw_text(0,60, "Up - move selected motor up at set speed")
    brick.screen.draw_text(0,80, "Down - move selected motor down at set speed")
    brick.screen.draw_text(0,100, "Center - stop program and exit to main selection")
