import w1thermsensor
import time

sensor = w1thermsensor.W1ThermSensor()
temperatures = sensor.get_temperatures([w1thermsensor.W1ThermSensor.DEGREES_F, w1thermsensor.W1ThermSensor.DEGREES_C, w1thermsensor.W1ThermSensor.KELVIN])
timestring = time.strftime("%y%m%d::%H:%M:%S")
print(timestring + (": ") + str(temperatures[0]) + " F  (" + str(temperatures[1]) + " C, " + str(temperatures[2]) + " K)")
