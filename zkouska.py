from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(1), freq=50)
button1 = Pin(2,Pin.IN)
button2 = Pin(3,Pin.IN)
button3 = Pin(4,Pin.IN)
rychlost = 0


def set_angle(angle):
    pulse_width = int(((angle * 2.5 + 500) / 20000) * 65535)
    servo.duty_u16(pulse_width)

while True:
        if button1.value() == 1:
            rychlost += 20
            sleep(0.1)  

        if button2.value() == 1:
            rychlost -= 20
            sleep(0.1)  

        if button3.value() == 1:
            set_angle(rychlost)

        if button3.value() == 0:
            servo.deinit()
            sleep(0.1)

