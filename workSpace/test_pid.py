import RTController
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import BSpline, make_interp_spline

def test_pid(P= 0.2, I= 0.0, D= 0.0, L= 100):
    pid = RTController.PID(P, I, D)
    pid.setPoint = 0.0
    pid.settings(s_rate=0.01)

    END = L
    feedback = 0
    fb_list = []
    t_list = []
    sp_list = []

    for i in range(1, END):
        pid.calcPID(feedback)
        print('==========='+str(i)+'=============')
        print("Setpoint: " + str(pid.setPoint))
        print("P: " + str(pid._P))
        print("I: " + str(pid._I))
        print("Output: " + str(pid.output))
        output = pid.output
        if pid.setPoint > 0:
            feedback += (output - (1/i))
        if i > 9:
            pid.setPoint = 1
        time.sleep(0.02)
        fb_list.append(feedback)
        sp_list.append(pid.setPoint)
        t_list.append(i)
    time_sm = np.array(t_list)
    time_smo = np.linspace(time_sm.min(), time_sm.max(), 300)
    helper_x3 = make_interp_spline(t_list, fb_list)
    fb_smo = helper_x3(time_smo)

    plt.plot(time_smo, fb_smo)
    plt.plot(t_list, sp_list)
    plt.xlim((0, L))
    plt.ylim((min(fb_list) - 0.5, max(fb_list) + 0.5))
    plt.xlabel('time (s)')
    plt.ylabel('PID (PV)')
    plt.title('TEST PID')

    plt.ylim((1 - 0.5, 1 + 0.5))

    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    test_pid(1.1, 2, 0.001, L=100)