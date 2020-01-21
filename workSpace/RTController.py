from RoutineInterfaceDataModel import Routine
import RoutineInterfaceDataModel
import time
from singletonType import uSingleton
import gc
try:
    import _thread
    from machine import Pin, PWM
    import max6677

except ImportError:
    from _machine import Pin, PWM
    pass
"""Proportional-Integral-Derivative Temperature controller minimal implementation in MicroPython"""
class PID(uSingleton):
    def __init__(self, p=0.2, i=0, d=0, c_time=None):
        self.p, self.i, self.d, self.s_rate = [p, i, d, 0.0]
        self.c_time = c_time if c_time != None else time.time()
        self.p_time = self.c_time
        self.rst()
    def SYSrst(self):
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


"""Abstraction layer for interacting with ESP32 hardware pins"""
class TempController(uSingleton):
    _Buf = {
        "Temp": None,
        "Fan": True,
        "Htr": False,
        "setPt": 0.0
    }

    def __init__(self, M_Pin= 15, H_Pin=16, F_Pin=17, T_temp=0.0):
        self.tempMsr_pin = M_Pin
        self.htrPWM_pin = H_Pin
        self.fan_pin = F_Pin
        self._Buf["setPt"] = T_temp

    @classmethod
    def measure(cls):
        #{INDEV}
        cls.temperature = time.time()
        return cls.temperature
    def respond(self):
        #{INDEV}
        pass
    @classmethod
    def rst(cls):
        #{INDEV}
        pass
    @property
    def temperature(self):
        return self._Buf["Temp"]
    @temperature.setter
    def temperature(self, v):
        self._Buf['Temp'] = v
    @property
    def fanState(self):
        return self._Buf["Fan"]
    @fanState.setter
    def fanState(self, v):
        self._Buf['setPt'] = v

"""Real-Time Controller object is the main interface between webservers and hardware"""

class RTController(uSingleton):
    _currentCyc = None
    _currentTemp = None
    _currentSP = None
    _thread = None
    _exit = False
    _time = None

    @staticmethod
    def runtimeControl(state=False):
        if state:
            pass
        else:
            print("System Reset")
            PID().SYSrst()
            TempController.rst()
            print("Exit Thread called")
            RTController._exit = True
            RTController._currentCyc = None
            RTController._currentTemp = None
            RTController._currentSP = None
            RTController._thread = None
            RTController._time = None
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
        if current.idx != 0:
            cls.runtimeControl(state=True)
            return True
        else:
            cls.runtimeControl(state=False)
            return False

    @classmethod
    def RTStart(cls):
        try:
            srt = cls.getSubRoutine()
        except IndexError:
            print("Thread Stopped")
            return
        cls._exit = False
        T_D = srt.temp_dur
        cy = srt.cycle
        pid = PID(1.1, 2, 0.001)
        for i in range(len(cy)):
            #print(i)
            for j in range(cy[i]):
                cls._currentCyc = j + 1
                #print(j)
                c_time = time.time()
                p_time = c_time
                d_time = c_time - p_time

                while d_time <= T_D[i][1] * 60:
                    print("Time Delta: ",d_time)
                    print("time target: ", T_D[i][1] * 60)
                    cls._currentSP = T_D[i][0]
                    pid.setPoint = cls._currentSP
                    cls._currentTemp = TempController.measure()
                    pid.calcPID(cls._currentTemp)
                    #print(cls._currentSP, cls._currentTemp, "PID: ", pid.output)
                    pwm = max(min(int(pid.output),100),0)
                    print("Target: %.1f C | Current: %.1f C | PWM: %s %% | PID: %s"%(cls._currentSP, cls._currentTemp, pwm, pid.output))
                    pmw0 = PWM(Pin(0))
                    if not cls._exit:
                        pass
                    else:
                        return

                    time.sleep(1)
                    d_time = time.time() - p_time
                    if int(d_time) % 60 == 0:
                        cls._time -= 1 # time is in minutes
                        print("Time Left: " + str(cls._time))


        print(T_D)
        cls.runtimeControl(state=False)
        return
    @classmethod
    def calcTime(cls):
        _total = 0
        if cls._time == None:
            try:
                srt = cls.getSubRoutine()
            except IndexError:
                print("Thread Stopped")
                return
            cls._exit = False
            T_D = srt.temp_dur
            cy = srt.cycle
            for i in range(len(cy)):
                _total += cy[i] * T_D[i][1]
            cls._time = _total
        print("Total Time: " + str(cls._time))
        return cls._time

    def currentCycle(self):
        return self._currentCyc

    def currentSetpoint(self):
        return self._currentSP

    def currentTemperature(self):
        return self._currentTemp

    def currentTotalTime(self):
        return self._time

if __name__ == '__main__':
    RoutineInterfaceDataModel.test(T=[40, 50], D=[1, 1], C=[1, 1])
    RTController.calcTime()
    RTController.RTStart()
