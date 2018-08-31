#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Física da Computação
#Carareto
#17/02/2018
#  Camada de Enlace
####################################################

# Importa pacote de tempo
import time

# Construct Struct
#from construct import *

# Interface Física
from interfaceFisica import fisica

# enlace Tx e Rx
from enlaceRx import RX
from enlaceTx import TX

class enlace(object):
    """ This class implements methods to the interface between Enlace and Application
    """

    def __init__(self, name):
        """ Initializes the enlace class
        """
        self.fisica      = fisica(name)
        self.rx          = RX(self.fisica)
        self.tx          = TX(self.fisica)
        self.connected   = False

    def enable(self):
        """ Enable reception and transmission
        """
        self.fisica.open()
        self.rx.threadStart()
        self.tx.threadStart()

    def disable(self):
        """ Disable reception and transmission
        """
        self.rx.threadKill()
        self.tx.threadKill()
        time.sleep(1)
        self.fisica.close()

    ################################
    # Application  interface       #
    ################################
    def sendData(self, data):
        """ Send data over the enlace interface
        """

        pacote, lenPayload = self.tx.cria_package(data, 4) #envia o pacote em sí
        self.tx.sendBuffer(pacote)
        return lenPayload


    def getData(self):
        """ Get n data over the enlace interface
        Return the byte array and the size of the buffer
        """
        print('entrou na leitura e tentara ler ')

        data , size= self.rx.getNData()
        payload, tipo, ok = self.rx.desfaz_package(data)
       
        return(payload, len(payload))

    def client_sync(self):
        sync1 = False
        sync2 = False
        payload = (0).to_bytes(1, byteorder = "big")
        sync_package = self.tx.cria_package(payload, 1)
        sync_package3 = self.tx.cria_package(payload, 3)

        self.tx.sendBuffer(sync_package)
        timer = time.time()
        while not sync1:
            data, size = self.rx.getNData()
            payload, tipo, ok = self.rx.desfaz_package(data)
            if tipo == 2 and ok:
                sync1 = True
                break    
            run_time = time.time() - timer
            if run_time > 5.0:
                print("Error: not receive type 2 ")
                self.tx.sendBuffer(sync_package)
                timer = time.time()
        self.tx.sendBuffer(sync_package3)     

    def server_sync(self):
        sync1 = False
        sync2 = False
        payload = (0).to_bytes(1, byteorder = "big")
        sync_package2 = self.tx.cria_package(payload, 2)

        while not sync1:
            data, size = self.rx.getNData()
            payload, tipo, ok, = self.rx.desfaz_package(data)
            if tipo == 1 and ok:
                sync1 = True
                break

        self.tx.sendBuffer(sync_package2)
        timer = time.time()
        while not sync2:
            data, size = self.rx.getNData()
            payload, tipo, ok = self.rx.desfaz_package(data)
            if tipo == 3 and ok:
                sync2 = True
                break
                
            run_time = time.time() - timer
            if run_time > 5.0:
                self.tx.sendBuffer(sync_package2)
                timer = time.time()
             
        def client_transmission(self,payload):
            payloadnulo = (0).to_bytes(1, byteorder = "big")
            sync_package3 = self.tx.cria_package(payloadnulo, 3)
            sync_package4 = self.tx.cria_package(payload, 4)
            sync_package5 = self.tx.cria_package(payloadnulo, 5)
            sync_package6 = self.tx.cria_package(payloadnulo, 6)
            self.tx.sendBuffer(sync_package4)
            sync1 = False
            while not sync1:
                data, size = self.rx.getNData()
                payload, tipo, ok, = self.rx.desfaz_package(data)
                if tipo == 2:
                    self.tx.sendBuffer(sync_package3)
                    self.tx.sendBuffer(sync_package4)
                elif tipo = 4:
                    print("Erro 1: Não recebimento da mensagem 5 ou 6.")
                    self.tx.sendBuffer(sync_package4)
                elif tipo == 5:
                    sync1 = True
                elif tipo == 6:
                    self.tx.sendBuffer(sync_package4)
                    

        def server_transmission(self):
            payloadnulo = (0).to_bytes(1, byteorder = "big")
            sync_package5 = self.tx.cria_package(payloadnulo, 5)
            sync_package6 = self.tx.cria_package(payloadnulo, 6)
            sync1 = False
            while not sync1:
                data, size = self.rx.getNData()
                payload, tipo, ok, = self.rx.desfaz_package(data)
                if tipo == 4 and ok:
                    self.tx.sendBuffer(sync_package5)
                    sync1 = True
                elif tipo == 4 and not ok:
                    self.tx.sendBuffer(sync_package6) 
                    sync1 = True 
        
            

