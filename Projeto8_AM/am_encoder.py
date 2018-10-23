import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal
from signalTeste import *

#Configurações iniciais
cutoff_hz = 4000.0
ripple_db = 60.0 #dB
t = 9 #tempo de duração da gravação
f_carrier = 2000 #MHz
fs = 44100

##########################

def generateSin(f1):
    fs = 44100
    t=9
    n = t*fs
    time = np.linspace(0, t, n)
    signal = np.sin(f1*time*2*np.pi)
    return signal, time

def normalize(data):
    dmax = max(data)
    dmin = min(data)
    normalized = []
    for i in range(len(data)):
        norma = (data[i]-dmin)/(dmax-dmin)
        normalized.append(norma)
    
    return normalized

def filtra_sinal(data, samplerate):
    nyq_rate = samplerate/2
    width = 5.0/nyq_rate
    N , beta = signal.kaiserord(ripple_db, width)
    taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
    yFiltrado = signal.lfilter(taps, 1.0, data)

    return yFiltrado


#exemplo de filtragem do sinal yAudioNormalizado
# https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html

signalMeu = signalMeu()
data, samplerate = sf.read('elikevin.wav')
raw_data = data[:,0]
t = np.linspace(0,t,len(raw_data))

normalized_data = normalize(raw_data)

f_signal = filtra_sinal(normalized_data, samplerate)
carrier = generateSin(f_carrier)
#modulated_signal = carrier*f_signal





#PLOTS
plt.plot(t, raw_data)
plt.title("Raw data")
plt.show()

plt.plot(t, normalized_data)
plt.title("Normalized data")
plt.show()

plt.plot(t, f_signal)
plt.title("Filtered signal")
plt.show()

#signalMeu.plotFFT(modulated_signal, fs)

#plt.plot(t,modulated_signal)
#plt.title("Modulated data")
#plt.show()
