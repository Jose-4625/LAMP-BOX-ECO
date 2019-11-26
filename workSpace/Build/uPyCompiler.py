import mpy_cross
import os
import shutil
workPath = '..'
if os.path.exists('../compiled'):
    pass
else:
    os.mkdir('../compiled')
if os.path.exists('../compiled/MicroWebSrv2'):
    pass
else:
    os.mkdir('../compiled/MicroWebSrv2')
if os.path.exists('../compiled/MicroWebSrv2/libs'):
    pass
else:
    os.mkdir('../compiled/MicroWebSrv2/libs')
if os.path.exists('../compiled/MicroWebSrv2/mods'):
    pass
else:
    os.mkdir('../compiled/MicroWebSrv2/mods')

for i in os.listdir(workPath):
    if i.endswith('.py') and i not in ['gzipper.py', 'main.py', 'test_pid.py']:
        print("Compiling: " + i)
        mpy_cross.run(workPath + '/' + i)


for i in os.listdir(workPath):
    print("cleaning workSpace...")
    if i.endswith('.mpy'):
        shutil.move(workPath + '/' + i, '../compiled/' + i)
    else:
        pass
#pack MicroWebSrv2 into bytecode
MWS = workPath+'/'+'MicroWebSrv2'
for i in os.listdir(MWS):
    if i.endswith('.py'):
        print("Compiling: " + i)
        mpy_cross.run(MWS + '/' + i)


for i in os.listdir(MWS):
    print("cleaning workSpace...")
    if i.endswith('.mpy'):
        try:
            shutil.move(MWS + '/' + i, '../compiled/MicroWebSrv2/' + i)
        except PermissionError:
            print("A problem occured while moving: "+ i +" Not Fatal")
    else:
        pass

MWS = workPath+'/MicroWebSrv2/' + 'libs'
for i in os.listdir(MWS):
    if i.endswith('.py'):
        print("Compiling: " + i)
        mpy_cross.run(MWS + '/' + i)


for i in os.listdir(MWS):
    print("cleaning workSpace...")
    if i.endswith('.mpy'):
        shutil.move(MWS + '/' + i, '../compiled/MicroWebSrv2/libs/' + i)
    else:
        pass

MWS = workPath+'/MicroWebSrv2/' + 'mods'
for i in os.listdir(MWS):
    if i.endswith('.py'):
        print("Compiling: " + i)
        mpy_cross.run(MWS + '/' + i)


for i in os.listdir(MWS):
    print("cleaning workSpace...")
    if i.endswith('.mpy'):
        shutil.move(MWS + '/' + i, '../compiled/MicroWebSrv2/mods/' + i)
    else:
        pass
print('Done, compiled mpy files can be found /compiled directory')


