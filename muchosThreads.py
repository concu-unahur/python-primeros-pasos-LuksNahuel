import threading
import time
import logging

from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir(secs):
    time.sleep(secs)

contador = Contador()
contador.iniciar()

threads = []

for i in range(10):
    #crear un thead
    #lanzarlo
    thread = threading.Thread(target=dormir, args=[1])
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()

contador.finalizar()
contador.imprimir()

# la ejecución tarda un segundo ya que crea los hilos uno tras otro
# casi a la misma vez y los espera a todos casi a la misma vez, por eso tarda 1 segundo el main thread