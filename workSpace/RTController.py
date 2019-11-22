from RoutineInterfaceDataModel import Routine
try:
    from machine import Pin
    import max6677
except ImportError:
    pass
#import PID
class TempController:
    def __init__(self, M_Pin= 15, H_Pin=16, F_Pin=17):
        self.tempMeasure_pin = M_Pin
        self.heaterPWM_pin = H_Pin
        self.fan_pin = F_Pin
    def measure(self):
        pass
    def responed(self):
        pass

class RTController(object):
    _currentSR = None
    @staticmethod
    def runtimeControl(state=False):
        pass
        #temperature controls
    @staticmethod
    def RT():
        Routine.show()
    @classmethod
    def getSubRoutine(cls):
       for i in Routine._subRoutines:
            print(i)
    @classmethod
    def RTCheck(cls, current):
        if current.idx == 1:
            cls.runtimeControl(state=True)
            pass
        elif current.idx == 0:
            cls.runtimeControl(state=False)

