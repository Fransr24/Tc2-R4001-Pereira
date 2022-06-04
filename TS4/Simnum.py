# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 21:58:32 2022

@author: perei
"""

import matplotlib.pyplot as plt  
import numpy as np  #
import scipy.signal as sig
from splane import analyze_sys, pretty_print_bicuad_omegayq

a = (1/((5**3)*4*0.34)) ##para dividirlo en las 3 transferencias

num = np.array([1, 0.068*a])
den = np.array([1, 0.068, 1.21])

num1 = np.array([1, 0.068*a])
den1 = np.array([1, 0.068, 1.21])
num2 = np.array([1, 0.056*a])
den2 = np.array([1, 0.056, 0.81])
num3 = np.array([1, 0.125*a])
den3 = np.array([1, 0.125, 1])

pretty_print_bicuad_omegayq(num1,den1)

mi_sos = sig.TransferFunction(num1,den1)

print (mi_sos)
plt.close('all')
analyze_sys(mi_sos, 'mi SOS')