from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,
                                GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Color,
                               SoundFile, Button)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Font
from .line_sensor import LineSensor
from .line_edge import LineEdge
brick = EV3Brick()
class Robot:
    def __init__(self):      
        """Class that represents the robot
        """
        try:

            self.state = "Port 1: Right Color"
            self.right_color = ColorSensor(Port.S1)

            self.state = "Port 2: Center Color"
            self.center_color = ColorSensor(Port.S2)

            self.state = "Port 3: Left Color"
            self.left_color = ColorSensor(Port.S3)

            self.state = "Port 4: Gyro"
            self.gyro = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
            
            self.state = "Port A: Left Motor"
            self.left_motor = Motor(Port.A)

            self.state = "Port B: Right Motor"
            self.right_motor = Motor(Port.B)

            self.state = "Port C: Linear Gear"
            self.linear_attachment_motor = Motor(Port.C)

            # self.state = "Port A: Yeeter"
            # self.yeeter_attachment_motor = Motor(Port.A)

            self.wheel_diameter = 55
            self.axle_track = 123
            self.drive_base = DriveBase(
                self.left_motor, self.right_motor, self.wheel_diameter, self.axle_track)
            self.state = "OK"
        except:
            brick.screen.clear()
            big_font = Font(size=18)
            brick.screen.set_font(big_font)        
            brick.screen.draw_text(0, 20, "Error!")
            brick.screen.draw_text(0, 40, self.state)    

    def display_sensor_values(self):
        """Displays sensor values
        """
        gyro_value = "Gyro    : {}".format(self.gyro.angle())
        left_color_value = "Left Color    : {}".format(self.left_color.reflection())
        right_color_value = "Right Color   : {}".format(self.right_color.reflection())
        center_color_value = "Center Color   : {}".format(self.center_color.reflection())

        big_font = Font(size=18)
        brick.screen.set_font(big_font)        
        brick.screen.clear()
        brick.screen.draw_text(0, 20, gyro_value)
        brick.screen.draw_text(0, 40, left_color_value)
        brick.screen.draw_text(0, 60, right_color_value)
        brick.screen.draw_text(0, 80, center_color_value)

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
            brick.speaker.beep(400 * beep_count, 100)
            wait(20)
    
    def drift_check(self):
        brick.speaker.beep(1200 , 500)
        wait(100)
        brick.speaker.beep(1200 , 500)
        drift = False
        start_gyro = self.gyro.angle()
        brick.screen.clear()
        big_font = Font(size=18)
        brick.screen.set_font(big_font)        
        brick.screen.draw_text(0, 20, "Checking Gyro drift...")

        wait(2000)

        if start_gyro != self.gyro.angle():
            brick.screen.draw_text(0, 60, "Error!")
            brick.screen.draw_text(0, 80, "Gyro drift")
            drift = True
        
        return drift

    def print_sensor_values(self):
        """Display robot sensor values. For debugging only
        """
        print("Gyro: ", self.gyro.angle())
        print("Left Color: ", self.left_color.reflection())
        print("Right Color: ", self.right_color.reflection())
        print("Center Color: ", self.center_color.reflection())

    def stop_motors(self):
        """ Stops all motors
        """
        self.left_motor.stop(Stop.BRAKE)
        self.right_motor.stop(Stop.BRAKE)
        self.linear_attachment_motor.stop(Stop.BRAKE)

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

        while pid.clock.time() < duration:
            # Calculatr error
            
            actual_angle = self.gyro.angle()
            error = (target_angle - actual_angle) % 360
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
        
        error = tolerance + 1
        min_speed = 50

        while abs(error) > tolerance:
            # Calculate error
            actual_angle = self.gyro.angle()
            error = (target_angle - actual_angle) % 360
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
            if which_sensor == LineSensor.CENTER:
                error = 50 - self.center_color.reflection()

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

    def stop_on_white(self, pid, speed, target_angle, which_sensor, color_value = 80):
        """ Gyro drives until given color sensor is on white

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
        if which_sensor == LineSensor.LEFT:
            sensor = self.left_color
        elif which_sensor == LineSensor.RIGHT:
            sensor = self.right_color
        else:
            sensor = self.center_color

        while sensor.reflection() < color_value:
            # Calculate error
            actual_angle = self.gyro.angle()
            error = (target_angle - actual_angle) % 360
            error = error - (360 * int(error / 180))

            # Calculate steering output
            steering = pid.compute_steering(error)

            # Drive the motors
            self.drive_base.drive(speed, steering)
            self.print_sensor_values

        # Stop motors
        self.drive_base.stop(Stop.BRAKE)
        
    def align(self, speed, sensor1, sensor2):
        """Aligns using color sensors on black line
        
        :param speed: The speed the robot moves at
        :type speed: Number
        :param sensor1: The first sensor the robot uses to align
        :type sensor1: Enum
        :param sensor2: The second sensor the robot uses to align
        :type sensor2: Enum
        """
        self.left_motor.run(speed)
        self.right_motor.run(speed)
        first_sensor = 0
        second_sensor = 0

        if sensor1 == LineSensor.LEFT:
            first_sensor = self.left_color
        elif sensor1 == LineSensor.RIGHT:
            first_sensor = self.right_color
        else:
            first_sensor = self.center_color

        if sensor2 == LineSensor.LEFT:
            second_sensor = self.left_color
        elif sensor2 == LineSensor.RIGHT:
            second_sensor = self.right_color
        else:
            second_sensor = self.center_color

        while True:
            first = False
            second = False
            if first_sensor.reflection() <= 10:
                self.left_motor.hold()
                first = True
            if second_sensor.reflection() <= 10:
                self.right_motor.hold()
                second = True
            if first and second == True:
                break

    def reset_sensors(self, reset_angle = 0):
        """Reset the robot's sensor values
        
        :param reset_angle: inital angle for the gyro, defaults to 0
        :type reset_angle: int, optional
        """
        # Resets the gyro
        self.gyro.reset_angle(reset_angle)

    def run_linear(self, speed, time, wait = True):
        """Runs linear gear
        
        :param speed: The speed the linear gear moves at
        :type speed: Number
        :param time: How long the linear gear runs for
        :type time: Number
        :param wait: Wait for action to complete before next step
        :type wait: Boolean
        """
        self.stop_motors()
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
        self.stop_motors()
        self.yeeter_attachment_motor.run_time(speed, time, Stop.BRAKE, wait)

    def move_yeeter(self, speed, rotations, wait = True):
        """Will calculate the ratio of the gears and then move the yeeter
         to a specific angle
        
        :param speed: The speed the yeeter moves at
        :type speed: Number
        :param rotations: How much the yeeter moves by in rotations
        :type rotations: Number
        :param wait: Wait for action to complete before next step
        :type wait: Boolean
        """
        self.stop_motors()
        target_angle = rotations*360
        self.yeeter_attachment_motor.run_angle(speed, target_angle * 5, Stop.BRAKE, wait)

    def move_linear(self, speed, rotations, wait = True):
        """Will calculate the ratio of the gears and then move the linear gear
         to a specific angle
        
        :param speed: The speed the linear gear moves at
        :type speed: Number
        :param rotations: How much the linear gear moves by in rotations
        :type rotations: Number
        :param wait: Wait for action to complete before next step
        :type wait: Boolean
        """
        self.stop_motors()
        target_angle = rotations*360
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
