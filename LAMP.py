from microwebsrv import MicroWebSrv
from machine import Pin
from esp import raw_temperature
ESP_temp = raw_temperature()
print(ESP_temp)


