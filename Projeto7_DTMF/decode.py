import picospy as np
import sounddevice as sd
import peakutils
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
from signalTeste import *
from encode import *

duration = 1
fs=44100

def Audio():
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()
    y = audio[:,0]
    X, Y = signalMeu.plotFFT(y, fs)
    picos = Picos(X, Y)
    PrintaTecla(picos)
    
def Picos(X, Y):
    picos = peakutils.indexes(Y, thres=0.05, min_dist=0)
    print(picos)
    return picos

def PrintaTecla(picos):
    if picos[0] and picos [1] in frequencia.um:
        print("Tecla Número 1")
    elif picos[0] and picos [1] in frequencia.dois:
        print("Tecla Número 2")
    elif picos[0] and picos [1] in frequencia.tres:
        print("Tecla Número 3")
    elif picos[0] and picos [1] in frequencia.quatro:
        print("Tecla Número 4")
    elif picos[0] and picos [1] in frequencia.cinco:
        print("Tecla Número 5")
    elif picos[0] and picos [1] in frequencia.seis:
        print("Tecla Número 6")
    elif picos[0] and picos [1] in frequencia.sete:
        print("Tecla Número 7")
    elif picos[0] and picos [1] in frequencia.oito:
        print("Tecla Número 8")
    elif picos[0] and picos [1] in frequencia.nove:
        print("Tecla Número 9")
    elif picos[0] and picos [1] in frequencia.zero:
        print("Tecla Número 0")

frequencia = Frequencia()
signalMeu = signalMeu()
Audio()