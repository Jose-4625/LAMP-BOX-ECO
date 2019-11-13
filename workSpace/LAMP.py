from MicroWebSrv2 import *
from time import sleep

@WebRoute(GET, '/')
def RequestTest(microWebSrv2, request):
    content = "./www/index.html.gz"

    request.Response.SetHeader('Accept-Encoding','gzip, deflate')
    request.Response.SetHeader('Content-Encoding','gzip')
    request.Response.SetHeader('Content-Type','application/x-gzip')
    request.Response.ReturnFile(content)

@WebRoute(GET, '/temp')
def RequestTest2(microWebSrv2, request):
    request.Response.ReturnOkJSON({
        'ClientAddr': request.UserAddress,
        'Accept': request.Accept,
        'UserAgent': request.UserAgent
    })


mws = MicroWebSrv2()
mws.SetEmbeddedConfig()
mws.BindAddress = ('127.0.0.1',3000)
mws.StartManaged()


try :
    while True :
        sleep(60)
except KeyboardInterrupt :
    print()
    mws.Stop()
    print('Bye')
    print()
