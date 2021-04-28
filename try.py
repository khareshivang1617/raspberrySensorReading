import Adafruit_DHT
import time
als = True
while als:
	print("......1")
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
	print("......2")
	if humidity is not None and temperature is not None:
		humidity = round(humidity, 2)
		temperature = round(temperature, 2)
		print("humidity = ", humidity, "\ntemperature = ", temperature, "\n")
	else:
		print("Can't connect to the sensor\n")
	print("......3")
	time.sleep(5)
