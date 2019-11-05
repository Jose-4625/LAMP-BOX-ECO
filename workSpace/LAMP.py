from microWebSrv import MicroWebSrv
try:
    from esp32  import raw_temperature, hall_sensor
    import uasyncio
except:
    from dummyESP32 import raw_temperature, hall_sensor
    import asyncio
#from os import urandom
ESP_temp = raw_temperature()
print("Current ESP32 Temp: " + str(ESP_temp))

async def _httpHandlerTEMPGet(httpClient, httpResponse):
  try:
    ESP_temp = raw_temperature()
    ESP_hall  = hall_sensor()
    print(ESP_temp, 'Temp')
    print(ESP_hall, 'Hall')
    data = [ESP_temp, ESP_hall]
  except:
    data = "Cannot read Temp sensor"
  httpResponse.WriteResponseOk(
    headers = ({'Cache-Control': 'no-cache'}),
    contentType = 'text/event-stream',
    contentCharset = 'UTF-8',
    content = data
  )
routeHandlers = [("/temp", "GET", _httpHandlerTEMPGet)]
srv = MicroWebSrv(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)
