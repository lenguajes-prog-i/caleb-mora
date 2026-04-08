import socket
import threading
HOST = "127.0.0.1"  
PORT = 5000 

# socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP - Perto
server.bind((HOST, PORT))

server.listen()

print("Servidor esperando conexión...")

#conn, addr = server.accept()
#print(f"Conexión establecida desde {addr}")

#data = conn.recv(1024).decode()
#print(f"Mensaje recibido: {data}")

#respuesta = "Mensaje recibido correctamente"
#conn.send(respuesta.encode())

#conn.close()
#server.close()
def manejar_cliente(cliente_socket, direccion):
    print(f"Cliente conectado desde {direccion}")
    while True:
        try:
            # recibir mensaje
            mensaje = cliente_socket.recv(1024).decode()
            if not mensaje:
                break
            print(f"Mensaje recibido de {direccion}: {mensaje}")
            # enviar respuesta
            respuesta = f"Hola cliente {direccion}, recibí tu mensaje: {mensaje}"
            cliente_socket.send(respuesta.encode())
        except ConnectionResetError:
            break
    print(f"Cliente desconectado desde {direccion}")
    cliente_socket.close()
while True:
    # aceptar conexiones
    cliente_socket, direccion = server.accept()
    # manejar cliente en un hilo separado
    hilo_cliente = threading.Thread(target=manejar_cliente, args=(cliente_socket, direccion))
    hilo_cliente.start()