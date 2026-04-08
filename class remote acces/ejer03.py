import pickle

class Auto():
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
    
    def __repr__(self):
        return f"El auto {self.modelo} tiene placa {self.placa}"
objeto_auto = Auto("Mazda", "ABC123")
objeto_auto1 = Auto("Chevrolet", "DEF456")
objeto_auto2 = Auto("Toyota", "GHI789")
objeto_auto3 = Auto("Nissan", "JKL012")
objeto_auto4 = Auto("peugeot", "LMN345")

auto = [objeto_auto,
        objeto_auto1,
        objeto_auto2,
        objeto_auto3,
        objeto_auto4]

#print(objeto_auto)
#print(objeto_auto1)
#print(objeto_auto2)
archivo_auto = open("autos.txt", "wb")
pickle.dump(auto, archivo_auto)
archivo_auto.close()

archivo_auto = open("autos.txt", "rb")
autos = pickle.load(archivo_auto)
archivo_auto.close()
for auto in autos:
    print(auto)
