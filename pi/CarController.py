import pigpio
import time

class CarModule:

    def __init__(self, 
                pi, 
                enable_speed_pin, 
                speed_pin_1, 
                speed_pin_2,
                enable_direction_pin,
                direction_pin_1,
                direction_pin_2,
                car_speed) :

        self.pi = pi

        if not self.pi.connected:
            print('Pi not connected. Exiting...')
            exit()

        self._high = 1
        self._low = 0

        self._car_speed = car_speed

        self._enable_speed_pin = enable_speed_pin
        self._speed_pin_1 = speed_pin_1
        self._speed_pin_2 = speed_pin_2

        self._enable_direction_pin = enable_direction_pin
        self._direction_pin_1 = direction_pin_1
        self._direction_pin_2 = direction_pin_2

        self.pi.set_mode(self._enable_speed_pin, pigpio.OUTPUT)
        self.pi.set_mode(self._speed_pin_1, pigpio.OUTPUT)
        self.pi.set_mode(self._speed_pin_2, pigpio.OUTPUT)
        self.pi.set_mode(self._enable_direction_pin, pigpio.OUTPUT)
        self.pi.set_mode(self._direction_pin_1, pigpio.OUTPUT)
        self.pi.set_mode(self._direction_pin_2, pigpio.OUTPUT)

        self.pi.write(self._enable_speed_pin, self._low)
        self.pi.write(self._enable_direction_pin, self._low)

    def forward(self) :
        self.pi.write(self._speed_pin_1, self._high)
        self.pi.write(self._speed_pin_2, self._low)
        self.pi.set_PWM_dutycycle(self._enable_speed_pin, self._car_speed)

    def backward(self) : 
        self.pi.write(self._speed_pin_1, self._low)
        self.pi.write(self._speed_pin_2, self._high)
        self.pi.set_PWM_dutycycle(self._enable_speed_pin, self._car_speed)

    def stop(self) :
        self.pi.write(self._speed_pin_1, self._low)
        self.pi.write(self._speed_pin_2, self._low)
        self.pi.write(self._enable_speed_pin, self._low)

    def left_turn(self) :
        self.pi.write(self._direction_pin_1, self._low)
        self.pi.write(self._direction_pin_2, self._high)
        self.pi.write(self._enable_direction_pin, self._high)

    def right_turn(self) :
        self.pi.write(self._direction_pin_1, self._high)
        self.pi.write(self._direction_pin_2, self._low)
        self.pi.write(self._enable_direction_pin, self._high)

    def straight_turn(self) : 
        self.pi.write(self._direction_pin_1, self._low)
        self.pi.write(self._direction_pin_2, self._low)
        self.pi.write(self._enable_direction_pin, self._low)