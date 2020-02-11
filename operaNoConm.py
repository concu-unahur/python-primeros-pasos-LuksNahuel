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
        #time.sleep(0.1)
        #lock.acquire()
        valor += 1
    finally:
        # finalmente lo libera para el segundo thread
        lock.release()

def multiplicarPorDos():
    global valor
    global lock
    lock.acquire()
    try:
        valor *= 2
    finally:
        lock.release()

lock.acquire()

t1 = threading.Thread(target=sumarUno, name="Sumar uno")
t2 = threading.Thread(target=multiplicarPorDos, name="Multiplicar por dos")

t2.start()
t1.start()

t2.join()

logging.info(valor)


