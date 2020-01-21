from upysh import *
def createFolders():
	mkdir('/www')
	mkdir('/MicroWebSrv2')
	cd('/MicroWebSrv2')
	mkdir('/MicroWebSrv2/mods')
	mkdir('/MicroWebSrv2/libs')
	cd('/')

def orderFiles():

	# web interface
	mv('./index.html','./www/index.html')
	# web server core
	mv('./webRoute.py','/MicroWebSrv2/webRoute.py')
	mv('./microWebSrv2.py','/MicroWebSrv2/microWebSrv2.py')
	mv('./httpResponse.py','/MicroWebSrv2/httpResponse.py')
	mv('./httpRequest.py','/MicroWebSrv2/httpRequest.py')
	mv('./__init__.py','/MicroWebSrv2/__init__.py')
	# web server modules 
	mv('./WebSockets.py','/MicroWebSrv2/mods/WebSockets.py')
	mv('./PyhtmlTemplate.py','/MicroWebSrv2/mods/PyhtmlTemplate.py')
	# web server libs
	mv('./XAsyncSockets.py','/MicroWebSrv2/libs/XAsyncSockets.py')
	mv('./urlUtils.py','/MicroWebSrv2/libs/urlUtils.py')
	
if pwd() == '/':
	createFolders()
	orderFiles()
else:
	cd('/')
	createFolders()
	orderFiles()

