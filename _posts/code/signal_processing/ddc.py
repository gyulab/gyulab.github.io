from math import log
from numpy import *
from scipy import signal
import matplotlib.pyplot as plt

#https://www.gibbard.me/cic_filters/cic_filters_ipython.html
#http://witestlab.poly.edu/~ffund/el9043/labs/lab1.html

def DigitalDownconverter(SamplingRate, Bandwidth, Centerfreq):
    n_taps = 64
    f_bw = Bandwidth
    Fs = SamplingRate
    
    len_datapart = length(datapart_T)/2
    I_datapart = zeros(len)
    Q_datapart = zeros(len)
    
    I_datapart_down = I_datapart * cos(2*pi*Centerfreq/Fs*arange(len_datapart))
    Q_datapart_down = Q_datapart * -sin(2*pi*Centerfreq/Fs*arange(len_datapart))

    LPF = signal.remez(n_taps, [0, f_bw, f_bw+(Fs/2-f_bw)/4, Fs/2], [1,0], Hz=Fs)
    I_datapart_LPF = signal.lfilter(LPF, 1.0, I_datapart_down)
    Q_datapart_LPF = signal.lfilter(LPF, 1.0, I_datapart_down)
    
    I_datapart = signal.resample(I_datapart_LPF, (2*f_bw)/(Fs/2))
    Q_datapart = signal.resample(Q_datapart_LPF, (2*f_bw)/(Fs/2))
    
    cplx_datapart = I_datapart + 1j*Q_datapart
    return cplx_datapart
    
    
