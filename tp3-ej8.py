"""
Ejercicio Nro 8
En matemáticas, particularmente en teoría de números o aritmética, 
un número primo es un número natural mayor que 1 
que tiene únicamente dos divisores distintos: 
él mismo y el 1. 
Diseñe un algoritmo que determine 
si un valor ingresado por el usuario es primo o no.
"""

def ingresar_numero() -> int:
    while True:
        try:
            return int(input("Ingrese un valor: "))
        except ValueError: 
            print("Debe ingresar un valor valido!")

"""
# Versión optimizada usando raíz cuadrada
import math

def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    
    return True

"""


def es_primo(numero: int) -> bool:
    if numero < 2:
        return False # Por definicion, los num menores a 2 no son primos.
    for i in range(2, (int(numero/2)+ 1)):
        if numero % i == 0:
            return False # Si encontro un divisor, NO ES PRIMO
        return True # Si se da que no encontro un divisor, SI ES PRIMO

def main() -> None:
    a = ingresar_numero()
    if es_primo(a):
        print(f"El numero {a} es primo")
    else: 
        print(f"El numero {a} NO es primo!")

if __name__ == "__main__":
    main()

