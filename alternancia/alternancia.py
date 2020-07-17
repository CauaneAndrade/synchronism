# Estrita Alternância
from threading import Thread
import time

global turn


def regiaoCritica():
    time.sleep(1)


def processamentoA(times, delay):
    global turn
    for x in range(times):
        print("Secao de Entrada A - ", x + 1)
        while (turn != 0):
            continue
        print("Regiao Critica A")
        regiaoCritica()
        print("Secao de Saida A")
        turn = 1
        print("Regiao nao critica A\n")
        time.sleep(delay)


def processamentoB(times, delay):
    global turn
    for x in range(times):
        print("Secao de Entrada B - ", x + 1)
        while (turn != 1):
            continue
        print("Regiao Critica B")
        regiaoCritica()
        print("Secao de Saida B")
        turn = 0
        print("Regiao nao critica B\n")
        time.sleep(delay)


print("Exemplo de Estrita Aternancia")
execTimes = 6
turn = 0

# no processamento você pode passar quantas vezes que a exec e
# qual o tempo de delay para simular o efeito comboi
tA = Thread(target=processamentoA, args=(execTimes, 1,))
tA.start()
tB = Thread(target=processamentoB, args=(execTimes, 3,))
tB.start()

u"""
a primeira `Thread` definida em `tA = Thread(target=processamentoA, args=(execTimes, 1,))`, recebe como `target` a função `processamentoA`
que espera dois parâmetros: um inteiro que define a quantidade de vezes que será excutado um loop e o segundo define a quantidade em segundo em que o programa suspenderá a execução da Thread.
No `processamentoA` há uma chamada para `regiaoCritica`, onde é chamado o sleep que supenderá a execução da Thread.

A segunda `Thread` definida em `tA = Thread(target=processamentoB, args=(execTimes, 5,))`, recebe como `target` a função `processamentoB`, que funciona de forma análoga à função `processamentoA`, difere nos valores da quantidade de vezes de execução do loop e o tempo de delay, onde a Thread é suspendida.

Percebe-se que ao chamar o método time.sleep, a Thread fica em modo de espera e outra Thread começa a ser executada. 
"""