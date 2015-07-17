class W1ThermSensor(object):
	#add more w1thermsensor mock functionality as needed

	THERM_SENSOR_DS18B20 = 0x28
	DEGREES_C = 0x01
	DEGREES_F = 0x02
	KELVIN = 0x03

	def get_temperature(self, unit=DEGREES_C):
		return 22.0

	def get_temperatures(self, units):
		return [22.0+i for i in range(len(units))]

	def __repr__(self):
		return "mock_sensor"