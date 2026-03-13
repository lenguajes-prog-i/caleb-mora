## hacer calculadora con funciones
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y
def main():
    print("Calculadora")
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Ingrese el número de la operación: ")

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Opción no válida")
if __name__ == "_main_":
    main()