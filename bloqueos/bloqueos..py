import threading

contador = 0
lock = threading.Lock()
#lock = threading.Semaphore()

def incrementador():
    global contador
    for _ in range(1000):
        with lock:
            contador += 1

hilo = threading.Thread(target=incrementador, args=())
hilo.start()
hilo2 = threading.Thread(target=incrementador, args=())
hilo2.start()

hilo.join()
hilo2.join()

print("Valor final del contador:", contador)