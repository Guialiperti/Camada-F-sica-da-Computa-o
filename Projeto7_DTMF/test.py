import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

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

def generateSin(f1, f2):
    t = 8
    fs = 44100
    n = t*fs
    time = np.linspace(0, t, n)
    signal_f1 = np.sin(f1*time*2*np.pi)
    signal_f2 = np.sin(f2*time*2*np.pi)
    soma = signal_f1 + signal_f2
    return soma, time

def som(list):
    f1 = list[0]
    f2 = list[1]
    soma, time = generateSin(f1, f2)

    plt.close("all")
    plt.plot(time, soma)
    plt.xlim(0,0.015)
    plt.xlabel('tempo')
    plt.ylabel('Onda')
    sd.play(soma, fs)
    sd.wait()
    plt.show()

fs = 44100
frequencia = Frequencia()

while True:
    print ("Input number:")
    num = int(input(""))
    if num == 1:
        som(frequencia.um)
    elif num == 2:
        som(frequencia.dois)
    elif num == 3:
        som(frequencia.tres)
    elif num == 4:
        som(frequencia.quatro)
    elif num == 5:
        som(frequencia.cinco)
    elif num == 6:
        som(frequencia.seis)
    elif num == 7:
        som(frequencia.sete)
    elif num == 8:
        som(frequencia.oito)
    elif num == 9:
        som(frequencia.nove)
    elif num == 0:
        som(frequencia.zero)