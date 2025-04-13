"""
Ejercicio Nro 11
Realizar un programa que permita ingresar números, 
hasta que el número ingresado no esté entre 1 y 100. 
Determinar el promedio de los números ingresados entre 1 y 50.
"""

def ingresar_numero() -> int:
    while True:
        try:
            return int(input("Ingrese un numero: "))
        except ValueError:
            print("Ingrese valores validos!")

def validar_numero_entre_1_y_100(numero: int) -> bool:
    return numero > 1 and numero < 100

def validar_numero_entre_1_y_50(numero: int) -> bool:
    return numero >= 1 and numero <= 50

def calcular_promedio(numero: int, suma: int, contador: int) -> tuple[int, int]:
    suma += numero
    contador += 1
    
    return suma, contador

def main() -> None:
    suma = 0
    contador = 0
    numero = ingresar_numero()

    while validar_numero_entre_1_y_100(numero):
        if validar_numero_entre_1_y_50(numero):
            suma, contador = calcular_promedio(numero, suma, contador)

        numero = ingresar_numero()

    if contador > 0:
        print(f"El promedio es: {suma / contador}")
    else: 
        print("No se ingresaro numeros entre 1 y 50")

if __name__ == "__main__":
    main()

