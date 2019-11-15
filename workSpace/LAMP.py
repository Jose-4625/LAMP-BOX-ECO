from MicroWebSrv2 import *
from time import sleep

#create webroute
@WebRoute(GET, '/')
def RequestTest(microWebSrv2, request):
    request.Response.SetHeader('Content-Encoding','gzip')
    request.Response.SetHeader('Content-Type','text/css')

    content = open("./www/index.html", 'r').read()
    request.Response.ReturnOk(content)
    print(request.Response._headers)
#Start Server
mws = MicroWebSrv2()
mws.SetEmbeddedConfig()
mws.AddMimeType('.gz','application/x-gzip')
mws.BindAddress = ('127.0.0.1',3000)
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
