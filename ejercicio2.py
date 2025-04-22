print("Calculadora")
print("1. Sumar")
print("2. Restar")
print("3. Multtiplicar")
print("4. Dividir")

opcion = 0
num1 = 0
num2 = 0
resultado = 0

opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    
    num1 = int(input("Ingrese el primer numero"))
    num2 = int(input("Ingrese el segundo numero"))
    resultado = num1 + num2

    print(f"El resultado de la suma es: {resultado}")

elif opcion == 2:
    print("restando")
else:
    print("Opcion ingresada no es valida")