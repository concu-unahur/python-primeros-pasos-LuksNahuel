import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

valor = 10
# Ahora los threads se esperan entre sí
lock = threading.Lock()

def sumarUno():
    global valor
    global lock
    try:
        # el thread toma el control y hace la operación
        lock.acquire()
        valor += 1
    finally:
        # finalmente lo libera para el segundo thread
        lock.release()

def multiplicarPorDos():
    global valor
    global lock
    try:
        lock.acquire()
        valor *= 2
    finally:
        lock.release()
        
t1 = threading.Thread(target=sumarUno)
t2 = threading.Thread(target=multiplicarPorDos)

t1.start()
t2.start()

logging.info(valor)


