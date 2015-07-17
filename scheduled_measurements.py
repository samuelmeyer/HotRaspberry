DEBUG_FLAG = True
if DEBUG_FLAG:
	import MockSensor as w1thermsensor
else:
	import w1thermsensor
import logging
import time
from apscheduler.schedulers.background import BackgroundScheduler

def get_temperatures(sensor):
	return sensor.get_temperatures([w1thermsensor.W1ThermSensor.DEGREES_F,
					w1thermsensor.W1ThermSensor.DEGREES_C, w1thermsensor.W1ThermSensor.KELVIN])

def check_and_log(sensor):
	temperatures = get_temperatures(sensor)
	date_string = time.strftime("%Y/%m/%d")
	time_string = time.strftime("%H:%M:%S")
	logging.info(" " + date_string + ", " + time_string + ", " + str(temperatures[0]) + ", "
		     + str(temperatures[1]) + ", " + str(temperatures[2]))


def main():
	logging.basicConfig(filename="temp.log", level=logging.INFO)
	logging.getLogger("apscheduler").setLevel(logging.WARN)
	sensor = w1thermsensor.W1ThermSensor()
	scheduler = BackgroundScheduler()
	scheduler.start()
	interval = 60.0
	scheduler.add_job(check_and_log, 'interval', seconds=interval, args=[sensor])
	while True:
		#TODO exception handling
		continue
	



if __name__ == "__main__":
	main()


