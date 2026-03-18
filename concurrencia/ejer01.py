#concurrencia: ejecutar varias tareas al mismo tiempo
import threading
import time

#print(threading.active_count())
#print(threading.enumerate())
def programar():
    print("Inicio 1")
    time.sleep(4)
    print("Finalizo 1")
def beber_agua():
    print("Inicio 2")
    time.sleep(6)
    print("Finalizo 2")
def estudiar():
    print("Inicio 3")
    time.sleep(4)
    print("Finalizo 3")

inicio = time.perf_counter()

#programar()
#beber_agua()
#estudiar()

#hilos: ejecutar varias tareas al mismo tiempo
hilo1_programar= threading.Thread(target=programar, args=())
hilo1_programar.start()
hilo2_beber_agua= threading.Thread(target=beber_agua, args=())
hilo2_beber_agua.start()
hilo3_estudiar= threading.Thread(target=estudiar, args=())
hilo3_estudiar.start()

hilo1_programar.join()
hilo2_beber_agua.join()
hilo3_estudiar.join()
fin = time.perf_counter()

tiempo = fin - inicio
print(tiempo)