import numpy as np
import sounddevice as sd
import peakutils
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
from signalTeste import *

duration = 1
fs=44100

def Audio():
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    y = audio[:,0]
    X, Y = signalMeu.plotFFT(y, fs)
    Picos(X, Y)
    


def Picos(X, Y):
    picos = peakutils.indexes(Y, thres=0.05, min_dist=0)
    print(picos)

signalMeu = signalMeu()
Audio()