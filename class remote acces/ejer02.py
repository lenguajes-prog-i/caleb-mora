import pickle

datos = {
    "nombre": "Cortes Perez Andres Steven",
    "materia": "Lenguaje de Programacion 1",
    "notas":[1,2,2.5,3]
}
with open("data.txt", "wb") as archivo:
    pickle.dump(datos, archivo)

with open("data.txt", "rb") as archivo2:
    datos_estudiantes = pickle.load(archivo2)
print(datos_estudiantes)