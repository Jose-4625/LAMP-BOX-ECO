from MicroWebSrv2 import *
from time import sleep
import json
from RoutineInterfaceDataModel import Routine
from RTController import RTController, TempController
import _thread
try:
    import esp
except ImportError:
    pass
class stream:
    def __init__(self,x):
        self.data = x.encode()
    def readinto(self,x):
        msg = self.data
        x[:len(msg)] = msg
        return len(msg)
    def close(self):
        return True

#create Interface webroute
@WebRoute(GET, '/')
def GETInterface(microWebSrv2, request):
    request.Response.SetHeader('Content-Encoding','gzip')
    request.Response.SetHeader('Content-Type','text/css')

    content = open("./www/index.html", 'r').read()
    request.Response.ReturnOk(content)
    print(request.Response._headers)

@WebRoute(POST, '/')
def POSTInterface(microWebSrv2, request):
    req = json.dumps(request.GetPostedJSONObject())
    interface = Routine.addSubRoutine(req)
    RTController.RTCheck(RTController.getSubRoutine())
    RTController.RT(_thread.start_new_thread(RTController.RTStart, ()))
    request.Response.ReturnOk()

@WebRoute(GET, "/live")
def GET_ESP_Data(microWebSrv2, request):
    try:
        c_t = TempController()
        c_t = c_t.measure()
        if all(isinstance(i, float) for i in [c_t]):  # Confirm values
            data = '{0:.1f}&deg;C'.format(c_t)
        else:
            data = 'Invalid reading.'

    except:
        data = 'Attempting to read sensor...'
    request.Response.SetHeader('Content-Type', 'text/event-stream')
    request.Response.ReturnOkJSON({
        'MeasuredTemp': data
    })
def restart():
    mws = MicroWebSrv2()
    mws.SetEmbeddedConfig()
    mws.AddMimeType('.gz', 'application/x-gzip')
    mws.BindAddress = ('127.0.0.1', 4000)
    mws.StartManaged()

    # keep server running
    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        print()
        mws.Stop()
        print('Bye')
        print()

#Start Server
mws = MicroWebSrv2()
mws.SetEmbeddedConfig()
mws.AddMimeType('.gz','application/x-gzip')
mws.BindAddress = ('127.0.0.1',4000)
mws.StartManaged()

#keep server running
try :
    while True :
        sleep(60)
except KeyboardInterrupt :
    print()
    mws.Stop()
    print('Bye')
    print()
