from RoutineInterfaceDataModel import Routine
import RoutineInterfaceDataModel
import time
import _thread
try:
    from machine import Pin
    import max6677
except ImportError:
    pass
class PID:
    _instances = []
    def __init__(self, p=0.2, i=0, d=0, c_time=None):
        self.p, self.i, self.d, self.s_rate = [p, i, d, 0.0]
        self.c_time = c_time if c_time != None else time.time()
        self.p_time = self.c_time
        self.rst()
        self._instances.append(self)
    @classmethod
    def SYSrst(cls):
        for i in cls._instances:
            i.rst()
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
    def __init__(self, M_Pin= 15, H_Pin=16, F_Pin=17, T_temp=0.0):
        self.tempMsr_pin = M_Pin
        self.htrPWM_pin = H_Pin
        self.fan_pin = F_Pin
        self.targetT = T_temp
    @classmethod
    def measure(cls):
        return time.time()
    def respond(self):
        pass
    @classmethod
    def rst(cls):
        pass

"""Real-Time Controller object is the main interface between webservers and hardware"""

class RTController(object):
    _currentCyc = None
    _currentTemp = None
    _currentSP = None
    _thread = None
    _exit = False
    @staticmethod
    def runtimeControl(state=False):
        if state:
            pass
        else:
            PID.SYSrst()
            TempController.rst()
            print(_thread.get_ident())
            print(RTController._thread)
            print("Exit Thread called")
            RTController._exit = True
            del Routine._subRoutines[:]

        #temperature controls
    @classmethod
    def RT(cls,thread):
        cls._thread = thread
        Routine.show()
    @classmethod
    def getSubRoutine(cls):
       return Routine._subRoutines[-1]
    @classmethod
    def RTCheck(cls, current):
        print("current", current)
        if current.__dict__['idx'] != 0:
            cls.runtimeControl(state=True)
            return True
        else:
            cls.runtimeControl(state=False)
            return False
    @classmethod
    def RTStart(cls):
        try:
            srt = cls.getSubRoutine().__dict__
        except IndexError:
            print("Thread Stopped")
            return
        cls._exit = False
        T_D = srt['temp_dur']
        cy = srt['cycle']
        for i in cy:
            #print(i)
            for j in range(i):
                cls._currentCyc = j
                #print(j)
                c_time = time.time()
                p_time = c_time
                d_time = c_time - p_time

                while d_time <= T_D[0][1] * 60:
                    print("Time Delta: ",d_time)
                    cls._currentSP = T_D[0][0]
                    cls._currentTemp = TempController.measure()
                    print(cls._currentSP, cls._currentTemp)
                    if not cls._exit:
                        pass
                    else:
                        return
                    time.sleep(1)
                    d_time = time.time() - p_time

        print(T_D)
        return

if __name__ == '__main__':
    RoutineInterfaceDataModel.test()
    RoutineInterfaceDataModel.test()
    RoutineInterfaceDataModel.test()
    RoutineInterfaceDataModel.test()
    RTController.RTStart()

