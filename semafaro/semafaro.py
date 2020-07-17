#Semáfaro
from threading import Thread,Semaphore
import time

s = Semaphore()

def regiaoCritica():
    time.sleep(1)

def processamentoA(times, delay):
    for x in range(times):
        print ("Secao de Entrada A - ",x+1)        
        s.acquire()
        print ("Regiao Critica A")        
        regiaoCritica()
        print ("Secao de Saida A")
        s.release()
        print ("Regiao nao critica A\n")
        time.sleep(delay)    

def processamentoB(times, delay):
    for x in range(times):
        print ("Secao de Entrada B - ",x+1)
        s.acquire()
        print ("Regiao Critica B")        
        regiaoCritica()
        print ("Secao de Saida B")
        s.release()
        print ("Regiao nao critica B\n")
        time.sleep(delay)


print ("Exemplo de Semafaro")
execTimes = 5

#no processamento você pode passar quantas vezes que a exec e
#qual o tempo de delay para simular o efeito comboi
tA = Thread(target=processamentoA, args=(execTimes,1,))
tA.start()
tB = Thread(target=processamentoB, args=(execTimes,5,))
tB.start()

u"""
- O `Semaphore` gerencia um contador interno que é decrementado por cada chamada `acquire()` e incrementado por cada chamada de `release()`. <br>
O contador nunca pode ficar abaixo de zero; quando `acquire()` descobre que é zero, ele bloqueia, esperando até que alguma outra thread chame `release()`.
"""