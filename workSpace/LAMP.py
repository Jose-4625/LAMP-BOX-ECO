from MicroWebSrv2 import *
from time import sleep
import json
from RoutineInterfaceDataModel import Routine
from RTController import RTController, TempController
import _thread
import gc
try:
    import esp
except ImportError:
    pass

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
    RTController.calcTime()
    RTController.RT(_thread.start_new_thread(RTController.RTStart, ()))
    request.Response.ReturnOk()

@WebRoute(GET, "/live")
def GET_ESP_Data(microWebSrv2, request):
    try:
        c_t = TempController()
        c_t = c_t.measure()
        rt = RTController()
        c_c = rt.currentCycle()
        c_s = rt.currentSetpoint()
        c_tt = rt.currentTotalTime()

        if isinstance(c_t, float):  # Confirm values
            temp = '{0:.1f}'.format(c_t)
        else:
            temp = 'Invalid reading.'
        if isinstance(c_c, (int, float)):  # Confirm values
            cycle = '{0:.1f}'.format(c_c)
        else:
            cycle = 'Invalid reading.'
        if isinstance(c_s, (int, float)):  # Confirm values
            setP = '{0:.1f}'.format(c_s)
        else:
            setP = 'Invalid reading.'
        if isinstance(c_tt, (int, float)):  # Confirm values
            tt = '{0:.1f}'.format(c_tt)
        else:
            tt = 'Invalid reading.'

    except:
        temp = 'Attempting to read sensor...'

    request.Response.SetHeader('Content-Type', 'text/event-stream')
    request.Response.ReturnOkJSON({
        'MeasuredTemp': temp,
        'currentSetP': setP,
        'currentCycle': cycle,
        'currentTotalTime': tt
    })
    gc.collect()
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
