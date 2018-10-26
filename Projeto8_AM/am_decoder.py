import numpy as np
import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy import signal

#Configurações iniciais
cutoff_hz = 4000.0
ripple_db = 60.0 #dB
t = 9 #tempo de duração da gravação
f_carrier = 14000.0 #Hz
fs = 44100

##########################

def filtra_sinal(data, samplerate):
    nyq_rate = samplerate/2
    width = 5.0/nyq_rate
    N , beta = signal.kaiserord(ripple_db, width)
    taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
    yFiltrado = signal.lfilter(taps, 1.0, data)

    return yFiltrado

def record():
    duration = 10
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    y = audio[:,0]