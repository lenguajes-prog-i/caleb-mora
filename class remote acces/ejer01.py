import pickle

data = {"mensaje": "Hola"}

#print (type(data))
serializacion = pickle.dumps(data)
print(serializacion)
mensaje = pickle.loads(serializacion)
print(mensaje)