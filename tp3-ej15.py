"""
Ejercicio Nro 15
Considerando que el producto entero dos números enteros positivos, a y b, 
puede expresarse como la suma sucesiva de a tantas veces como indique b, 
diseñe un algoritmo que 
calcule el producto entre a y b mediante sumas sucesivas.
"""

def ingresar_numero() -> int:
    while True:
        try:
            return input("Ingrese un numero: ")
        except ValueError:
            print("Ingrese valores validos!")

def 