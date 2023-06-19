# VL53L1X ToF sensor basic distance measurement example.
from machine import I2C
from vl53l1x import VL53L1X
import time

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.skip_frames(time = 2000)

tof = VL53L1X(I2C(2))
clock = time.clock()
while True:
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
    print(f"Distance: {tof.read()}mm")
