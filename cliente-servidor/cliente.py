import socket

HOST = "10.59.75.58"
PORT = 5000

# socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexion
client.connect((HOST, PORT))

# mensaje
mensaje = "Marica, soy el cliente 1"
client.send(mensaje.encode())

# repuesta
respuesta = client.recv(1024).decode()
print(f"Respuesta del servidor: {respuesta}")

client.close()
