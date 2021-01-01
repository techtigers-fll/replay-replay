from pybricks.hubs import Ev3Brick
from pybricks.ev3devices import (Motor, ColorSensor,
                                GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Color,
                               SoundFile, Button)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font
from .line_sensor import LineSensor
from .line_edge import LineEdge
brick = Ev3Brick()
class Robot:
    def __init__(self):      
        """Class that represents the robot
        """
        try:

            self.state = "Port 1: Left Color"
            self.left_color = ColorSensor(Port.S1)

            self.state = "Port 2: Right Color"
            self.right_color = ColorSensor(Port.S2)

            self.state = "Port 3: Right Gyro"
            self.right_gyro = GyroSensor(Port.S3, Direction.COUNTERCLOCKWISE)
    
            self.state = "Port 4: Left Gyro"    
            self.left_gyro = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
            
            # self.state = "Port A: Yeeter"
            # self.yeeter_attachment_motor = Motor(Port.A)
            
            self.state = "Port B: Left Motor"
            self.left_motor = Motor(Port.B)

            self.state = "Port C: Right Motor"
            self.right_motor = Motor(Port.C)

            # self.state = "Port D: Linear Gear"
            # self.linear_attachment_motor = Motor(Port.D)

            self.wheel_diameter = 55
            self.axle_track = 120
            self.drive_base = DriveBase(
                self.left_motor, self.right_motor, self.wheel_diameter, self.axle_track)
            self.state = "OK"
        except:
            brick.display.clear()
            brick.display.text("Error!", (0, 20))
            brick.display.text(self.state, (0, 40))    

    def display_sensor_values(self):
        """Displays sensor values
        """
        left_gyro_value = "Left Gyro     : {}".format(self.left_gyro.angle())
        right_gyro_value = "Right Gyro    : {}".format(self.right_gyro.angle())
        gyro_average_value = "Average Gyro  : {}".format(self.gyro_average())
        left_color_value = "Left Color    : {}".format(self.left_color.reflection())
        right_color_value = "Right Color   : {}".format(self.right_color.reflection())

        big_font = Font(size=24)
        ev3.screen.set_font(x`)        
        brick.screen.clear()
        brick.screen.draw_text(left_gyro_value, (0, 20))
        brick.screen.draw_text(right_gyro_value, (0, 40))
        brick.screen.draw_text(gyro_average_value, (0, 60)) 
        brick.screen.draw_text(left_color_value, (0, 80))
        brick.screen.draw_text(right_color_value, (0, 100))

    def is_ok(self):
        """Tells if all sensors are plugged in
        
        :return: Checks the state of the sensors
        :rtype: Boolean
        """
        return self.state == "OK"

    def beep(self, is_down = False):
        """Plays a series of beeps
        
        :param is_down: Tells if to play series downwards, defaults to False
        :type is_down: bool, optional
        """
        beep_counts = range(1, 7) if not is_down else range(6, 0, -1)
        for beep_count in beep_counts:
            brick.sound.beep(400 * beep_count, 100)
            wait(20)
    
    def drift_check(self):
        brick.sound.beep(1200 , 500)
        wait(100)
        brick.sound.beep(1200 , 500)
        drift = False
        start_left_gyro = self.left_gyro.angle()
        start_right_gyro = self.right_gyro.angle()
        brick.display.clear()
        brick.display.text("Checking Gyro drift...", (0, 20))

        wait(2000)
        
        if start_left_gyro != self.left_gyro.angle():
            brick.display.text("Error!", (0, 40))
            brick.display.text("Left Gyro drift", (0, 60))
            drift = True

        if start_right_gyro != self.right_gyro.angle():
            brick.display.text("Error!", (0, 80))
            brick.display.text("Right Gyro drift", (0, 100))
            drift = True
        
        return drift

    def gyro_average(self):
        """Averages both gyro values and computes the modulo of the average.
        We use 2 gyros because it is more consistent.

        :return: Averaged gyro value
        :rtype: Number
        """
        left_angle = self.left_gyro.angle()
        right_angle = self.right_gyro.angle()
        angle = (left_angle + right_angle)/2
        return angle % 360

    def print_sensor_values(self):
        """Display robot sensor values. For debugging only
        """
        print("Gyro Average: ", self.gyro_average())
        print("Left Gyro: ", self.left_gyro.angle())
        print("Right Gyro: ", self.right_gyro.angle())
        print("Left Color: ", self.left_color.reflection())
        print("Right Color: ", self.right_color.reflection())

    def drive(self, pid, speed, target_angle, duration):
        """Drives the robot using a gyro to a specific angle    

        :param pid: Uses Pid instance with parameters set beforehand
        :type pid: Class
        :param speed: Speed of the robot
        :type speed: Number
        :param target_angle: Angle to drive the robot at
        :type target_angle: Number
        :param duration: Duration the function is run
        :type duration: Number
        """
        # Inititialize values
        pid.reset()
        target_angle = target_angle % 360

        while pid.clock.time() < duration:
            # Calculate error
            actual_angle = self.gyro_average()
            error = target_angle - actual_angle
            error = error - (360 * int(error / 180))

            # Calculate steering output
            steering = pid.compute_steering(error)

            # Drive the motors
            self.drive_base.drive(speed, steering)
            self.print_sensor_values

        # Stop motors
        self.drive_base.stop(Stop.BRAKE)

    def drive_dead_reckon(self, speed, duration, steering = 0):
        self.drive_base.drive(speed, steering)
        wait(duration)
        self.drive_base.stop(Stop.BRAKE)

    def turn(self, pid, target_angle, tolerance = 1):
        """Turns the robot to a specific angle.

        :param pid: Uses Pid instance with parameters set beforehand
        :type pid: Number
        :param target_angle: Angle the robot turns to
        :type target_angle: Number
        :param tolerance: How close to the target angle you want the robot to be
        :type tolerance: Number
        """

        # Inititialize values
        pid.reset()
        
        target_angle = target_angle % 360
        error = tolerance + 1
        min_speed = 50

        while abs(error) > tolerance:
            # Calculate error
            actual_angle = self.gyro_average()
            error = target_angle - actual_angle
            error = error - (360 * int(error / 180))

            # Call Pid compute_steering
            steering = pid.compute_steering(error) * -1

            # Set speed using a min_speed
            right_speed = max(min_speed, abs(steering))
            if steering < 0:
                right_speed = -1 * right_speed
            left_speed = -1 * right_speed

            # Run motors
            self.left_motor.run(left_speed)
            self.right_motor.run(right_speed)

        # Stop motors
        self.left_motor.stop()
        self.right_motor.stop()
        
    def follow_line(self, pid, speed, duration, which_sensor, which_edge):
        """Follows the line using a color sensor.

        :param pid: Uses Pid instance with parameters set beforehand
        :type pid: Pid
        :param speed: Speed of the Robot
        :type speed: Number
        :param duration: Duration of the function
        :type duration: Number
        :param which_sensor: The sensor the robot uses to follow the line
        :type which_sensor: LineSensor
        :param which_edge: Which side the white is on relative to the robot
        :type which_edge: LineEdge
        """
        
        # Inititialize values
        pid.reset()

        while pid.clock.time() < duration:
            # Selecting which sensor to use using an Enum
            if which_sensor == LineSensor.RIGHT:
                error = 50 - self.right_color.reflection()
            if which_sensor == LineSensor.LEFT:
                error = 50 - self.left_color.reflection()

            # Selecting which edge of the line to use
            if which_edge == LineEdge.RIGHT:
                pass
            else:
                error = error * -1

            # Calculate steering
            steering = pid.compute_steering(error)
            
            # Run motors
            self.drive_base.drive(speed, steering)

        self.drive_base.stop(Stop.BRAKE)

    def stop_on_white(self, pid, speed, target_angle, which_sensor, color_value = 90):
        """ Gyro drives until given color sensor is on black

        :param pid: PID setting of drive
        :type pid: Number
        :param speed: The speed the robot moves at
        :type speed: Number
        :param target_angle: the angle the gyro drives at
        :type target_angle: 
        :param which_sensor: Chooses which color sensor to use
        :type which_sensor: Enum
        :param color_value: The value of color that the robot stops at
        :type color_value: Number
        """
        # Inititialize values
        sensor = 0
        pid.reset()
        target_angle = target_angle % 360
        sensor = self.left_color if which_sensor == LineSensor.LEFT else self.right_color

        while sensor.reflection() < color_value:
            # Calculate error
            actual_angle = self.gyro_average()
            error = target_angle - actual_angle
            error = error - (360 * int(error / 180))

            # Calculate steering output
            steering = pid.compute_steering(error)

            # Drive the motors
            self.drive_base.drive(speed, steering)
            self.print_sensor_values

        # Stop motors
        self.drive_base.stop(Stop.BRAKE)
        
    def align(self, speed):
        """Aligns using color sensors on black line
        
        :param speed: The speed the robot moves at
        :type speed: Number
        """
        self.left_motor.run(speed)
        self.right_motor.run(speed)
        while True:
            left = False
            right = False
            if self.left_color.reflection() <= 10:
                self.left_motor.stop()
                left = True
            if self.right_color.reflection() <= 10:
                self.right_motor.stop()
                right = True
            if left and right == True:
                break

    def reset_sensors(self, reset_angle = 0):
        """Reset the robot's sensor values
        
        :param reset_angle: inital angle for the gyro, defaults to 0
        :type reset_angle: int, optional
        """
        # Resets the gyros
        self.left_gyro.reset_angle(reset_angle)
        self.right_gyro.reset_angle(reset_angle)

    def run_linear(self, speed, time, wait = True):
        """Runs linear gear
        
        :param speed: The speed the linear gear moves at
        :type speed: Number
        :param time: How long the linear gear runs for
        :type time: Number
        :param wait: Wait for action to complete before next step
        :type wait: Boolean
        """
        self.linear_attachment_motor.run_time(speed, time, Stop.BRAKE, wait)

    def run_yeeter(self, speed, time, wait = True):
        """Runs yeeter
        
        :param speed: The speed the yeeter moves at
        :type speed: Number
        :param time: How long the yeeter runs for
        :type time: Number
        :param wait: Wait for action to complete before next step
        :type wait: Boolean
        """
        self.yeeter_attachment_motor.run_time(speed, time, Stop.BRAKE, wait)

    def move_yeeter(self, speed, target_angle, wait = True):
        """Will calculate the ratio of the gears and then move the yeeter
         to a specific angle
        
        :param speed: The speed the yeeter moves at
        :type speed: Number
        :param angle: How much the yeeter moves by in degrees
        :type angle: Number
        :param wait: Wait for action to complete before next step
        :type wait: Boolean
        """
        self.yeeter_attachment_motor.run_angle(speed, target_angle * 5, Stop.BRAKE, wait)

    def move_linear(self, speed, target_angle, wait = True):
        """Will calculate the ratio of the gears and then move the linear gear
         to a specific angle
        
        :param speed: The speed the linear gear moves at
        :type speed: Number
        :param angle: How much the linear gear moves by in degrees
        :type angle: Number
        :param wait: Wait for action to complete before next step
        :type wait: Boolean
        """
        self.linear_attachment_motor.run_angle(speed, target_angle, Stop.BRAKE, wait)


    def pulse_yeeter(self, duration, count):
        """Pulses yeeter up and down a specific amount of times
        
        :param duration: How long each pulse lasts
        :type duration: Number
        :param count: Amount of pulses
        :type count: Number
        """
        counter = 1
        while counter <= count:
            self.run_yeeter(2000, duration)
            self.run_yeeter(-4000, duration)
            counter += 1
            wait(200)