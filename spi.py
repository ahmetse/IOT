import spidev
import time
import os
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
light_channel = 0
delay = 5

while True:
  light_level = ReadChannel(light_channel)
  print(light_level)
  time.sleep(delay)
