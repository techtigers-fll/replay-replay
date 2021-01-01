from pybricks.tools import StopWatch

class Pid:
    def __init__(self, kp, ki, kd):
        """Class that can be used to do PID calculations.

        :param kp: Proportional multiplier for the error
        :type kp: Number
        :param ki: Multiplier for the intergral of the error 
        :type ki: Number
        :param kd: Multiplier for the derivative of the error
        :type kd: Number
        """
        self.clock = StopWatch()
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.last_error = 0
        self.total_error = 0
        self.last_time = 0
    
    def reset(self):
        """Reset parameters before start of PID loop
        """
        self.clock.reset()
        self.last_time = self.clock.time()
        self.last_error = 0
        self.total_error = 0
       

    def compute_steering(self, error):
        """Computes and returns the corrections.

        :param error: Difference between target and actual angles
        :type error: Number
        :return: Returns correction value
        :rtype: Number
        """
        current_time = self.clock.time()
        elapsed_time = current_time - self.last_time
        self.last_time = current_time
        error_change = 0

        if elapsed_time > 0:
            error_change = (error - self.last_error)/elapsed_time
            self.total_error = self.last_error * elapsed_time + self.total_error

        self.last_error = error

        steering = error * self.kp
        steering += error_change * self.kd
        steering += self.total_error * self.ki/100

        return steering
