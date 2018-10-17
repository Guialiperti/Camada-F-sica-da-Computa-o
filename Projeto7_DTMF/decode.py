
import numpy as np
import sounddevice as sd
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
    signalMeu.plotFFT(y, fs)
    


signalMeu = signalMeu()
Audio()