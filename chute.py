#1 ele vai escolher um numero aleatorio de 1 ate 100
#2 vc vai ter que chutar um numero 
#3 avisar se o numero esta perto ou longe de acertar
import random
import time
import os
class Chute:
    def __init__(self) -> None:
        self.tentativa=0
        self.chute1=0
        self.numeroaleatorio=1
        self.numeromaximo=100
        self.teste=True
    def iniciar(self):
        self.numero()
        self.chute()
        while self.teste==True:
            if int(self.valordochute)<self.chute1:
                print('chute um numero maior')
                self.chute()
                self.tentativa+=1
            elif int(self.valordochute)>self.chute1:
                print('chute um valor mais baixo')
                self.chute()
                self.tentativa+=1
            if int(self.valordochute)==self.chute1:
                self.teste=False
                print('vc acertou')
                print('vc tentou ',self.tentativa)
    def numero(self):
        self.chute1=random.randint(self.numeroaleatorio,self.numeromaximo)
    def chute(self):
        self.valordochute=input('chute um numero:')

o=Chute()
o.iniciar()