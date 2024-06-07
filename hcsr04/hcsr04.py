from machine import Pin, time_pulse_us
import time

class HCSR04:
    def __init__(self, trig: Pin, echo: Pin, c:float = 340.0):
        self.trig = trig
        self.echo = echo
        self.c = c
        self.trig.value(0)
    
    def measure(self) -> float:
        time.sleep_us(3)
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)
        t = time_pulse_us(self.echo, 1, 30000)
        d = self.c * t / 20000.0
        # d = (t / 2) / 29.4
        return d

