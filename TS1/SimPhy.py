# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:29:43 2022

@author: perei
"""

import matplotlib.pyplot as plt  
import numpy as np  #
import scipy.signal as sig
import splane as tc2

w0 = 1
w1 = -1
e = 0.508


num = np.array([ 1, 0, 9])
den = np.array([ 1, 6, 12, 9])


mi_sos = sig.TransferFunction(num,den)

sos_pba = tc2.tf2sos_analog(num,den)
tc2.pretty_print_SOS(sos_pba)

print (mi_sos)
plt.close('all')
tc2.analyze_sys(mi_sos, 'mi SOS')


# # Codigo para probar si a una buena escala funciona bien
# from scipy import signal
# import matplotlib.pyplot as plt
# sys = signal.TransferFunction([1,-1], [1, 1])
# w, mag, phase = signal.bode(sys)
# plt.figure()
# plt.ylim(-1,1)
# plt.semilogx(w, mag)    # Bode magnitude plot
# plt.figure()
# plt.semilogx(w, phase)  # Bode phase plot
# plt.show()