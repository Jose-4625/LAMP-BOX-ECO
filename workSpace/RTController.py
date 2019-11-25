from RoutineInterfaceDataModel import Routine
import time
try:
    from machine import Pin
    import max6677
except ImportError:
    pass
class PID:
    def __init__(self, p=0.2, i=0, d=0, c_time=None):
        self.p, self.i, self.d, self.s_rate = [p, i, d, 0.0]
        self.c_time = c_time if c_time != None else time.time()
        self.p_time = self.c_time
        self.rst()
    def rst(self):
        self.setPoint, self._I, self._D, self._P, self.p_err, self.i_err, self.output, self.w_pro = [0,0,0,0,0,0,0,20]
    def calcPID(self, fb_val, c_time=None):
        err = self.setPoint - fb_val
        self.c_time = c_time if c_time != None else time.time()
        d_time = self.c_time - self.p_time
        d_err = err - self.p_err
        if d_time >= self.s_rate:
            self._P = self.p * err
            self._I += err * d_time
            if (-self.w_pro) > self._I:
                self._I = -self.w_pro
            elif self.w_pro < self._I:
                self._I = self.w_pro
            self._D = 0.0
            if d_time > 0:
                self._D = d_err / d_time
            self.p_time, self.p_err = self.c_time, err
            self.output = self._P + (self.i * self._I) + (self.d * self._D)
    def settings(self,i_gain=0,p_gain=0,d_gain=0,s_rate=0,w_pro=0):
        if i_gain:
            self.i = i_gain
        if p_gain:
            self.p = p_gain
        if d_gain:
            self.d = d_gain
        if s_rate:
            self.s_rate = s_rate
        if w_pro:
            self.w_pro = w_pro





class TempController:
    def __init__(self, M_Pin= 15, H_Pin=16, F_Pin=17):
        self.tempMeasure_pin = M_Pin
        self.heaterPWM_pin = H_Pin
        self.fan_pin = F_Pin
    def measure(self):
        pass
    def respond(self):
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

