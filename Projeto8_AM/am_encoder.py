import numpy as np
import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy import signal

#Configurações iniciais
cutoff_hz = 4000.0
ripple_db = 60.0 #dB
t = 9 #tempo de duração da gravação
f_carrier = 4000.0 #MHz
fs = 44100

##########################

def generateSin(f1,t):
    fs = 44100
    n = t*fs
    time = np.linspace(0, t, n)
    signal = 0.1 * np.sin(f1*time*2*np.pi)
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

data, samplerate = sf.read('elikevin.wav')
raw_data = data[:,0]
t = np.linspace(0,t,len(raw_data))
tempo_audio = len(raw_data)/44100

normalized_data = normalize(raw_data)

f_signal = filtra_sinal(normalized_data, samplerate)

carrier, timez = generateSin(f_carrier, tempo_audio)

modulated_signal = carrier*f_signal + carrier
sd.play(modulated_signal,fs)





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

plt.plot(t,modulated_signal)
plt.title("Modulated data")
plt.xlim(1.0, 1.05)
plt.show()
