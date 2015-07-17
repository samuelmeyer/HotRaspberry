DEBUG_FLAG = False
if DEBUG_FLAG:
	import MockSensor as w1thermsensor
else:
	import w1thermsensor
import logging
import time
from apscheduler.schedulers.background import BackgroundScheduler
import boto3
import html_generator

def get_temperatures(sensor):
	return sensor.get_temperatures([w1thermsensor.W1ThermSensor.DEGREES_F,
					w1thermsensor.W1ThermSensor.DEGREES_C, w1thermsensor.W1ThermSensor.KELVIN])

def check_and_log(sensor):
	temperatures = get_temperatures(sensor)
	date_string = time.strftime("%Y/%m/%d")
	time_string = time.strftime("%H:%M:%S")
	logging.info(" " + date_string + ", " + time_string + ", " + str(temperatures[0]) + ", "
		     + str(temperatures[1]) + ", " + str(temperatures[2]))
	update_website(temperatures, date_string, time_string)

def update_website(temperatures, date_string, time_string):
	#TODO use python objects instead of writing to and pushing file
	html = html_generator.make_html(temperatures[0], time_string, date_string)
	with open("scheduled_measurements_temporary.html", "w+") as f:
		f.write(html)
	s3 = boto3.resource('s3').Object('samuelmeyer.com','index.html')
	s3.put(Body=open('scheduled_measurements_temporary.html','rb'),ContentType="")


def main():
	logging.basicConfig(filename="temp.log", level=logging.INFO)
	logging.getLogger("apscheduler").setLevel(logging.WARN)
	logging.getLogger("botocore").setLevel(logging.WARN)
	logging.getLogger("boto3").setLevel(logging.WARN)
	sensor = w1thermsensor.W1ThermSensor()
	scheduler = BackgroundScheduler()
	check_and_log(sensor)
	scheduler.start()
	interval = 180.0
	scheduler.add_job(check_and_log, 'interval', seconds=interval, args=[sensor])
	while True:
		#TODO exception handling
		continue
	



if __name__ == "__main__":
	main()


