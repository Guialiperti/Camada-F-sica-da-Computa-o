import numpy as np
import sounddevice as sd
import peakutils
import time
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
from signalTeste import *


class Frequencia():# montagem da tabela de frequencias
    def __init__(self):
        
        self.keypadF =[[1209, 1336, 1477, 1633],
                        [697, 770, 852, 941]]

        self.um = [1209, 697]
        self.dois = [1336, 697]
        self.tres = [1477, 697]
        self.quatro = [1209, 770]
        self.cinco = [1336, 770]
        self.seis = [1477, 770]
        self.sete = [1209, 852]
        self.oito = [1336, 852]
        self.nove = [1477, 852]
        self.zero = [1336, 941]


duration = 1
fs=44100

def Audio():
    t = 1
    fs = 44100
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    y = audio[:,0]
    g, h = signalMeu.calcFFT(y, fs)
    ver_picos = Picos(g, h)
    valido = PrintaTecla(ver_picos, True)
    time = np.linspace(0, t, len(y))
    if valido:
        PrintaTecla(ver_picos, False)
        signalMeu.plotFFT(y, fs)
        plt.plot(time, y)
        plt.xlim(0.4,0.425)
        plt.ylim(-1,1)
        plt.show()
    else:
        pass
    
def Picos(X, Y):
    picos = peakutils.indexes(Y, thres=0.05, min_dist=0)
    print(picos)
    return picos

def PrintaTecla(picos, verifica):
    tecla = 100
    if picos[0] in frequencia.um and picos [1] in frequencia.um:
        tecla = 1
    elif picos[0] in frequencia.dois and picos [1] in frequencia.dois:
        tecla = 2
    elif picos[0] in frequencia.tres and picos [1] in frequencia.tres:
        tecla = 3
    elif picos[0] in frequencia.quatro and picos [1] in frequencia.quatro:
        tecla = 4
    elif picos[0] in frequencia.cinco and picos [1] in frequencia.cinco:
        tecla = 5
    elif picos[0] in frequencia.seis and picos [1] in frequencia.seis:
        tecla = 6
    elif picos[0] in frequencia.sete and picos [1] in frequencia.sete:
        tecla = 7
    elif picos[0] in frequencia.oito and picos [1] in frequencia.oito:
        tecla = 8
    elif picos[0] in frequencia.nove and picos [1] in frequencia.nove:
        tecla = 9
    elif picos[0] in frequencia.zero and picos [1] in frequencia.zero:
        tecla = 0
    if verifica:
        if tecla != 100:
            return True
        else:
            print("Harmonicos compativeis nao encontrados")
    else:
        print("Tecla:{0}".format(tecla))

frequencia = Frequencia()
signalMeu = signalMeu()

tempo = time.time()
break_time = time.time()
while True:
    tempo_corrido = time.time() - tempo
    if tempo_corrido > 1.0:
        Audio()
        tempo = time.time()
    if time.time() - break_time > 15:
        break
