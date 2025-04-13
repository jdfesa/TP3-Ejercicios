"""
Ejercicio Nro 6
Realizar un programa que permita ingresar números 
y determinar si el número es par o no. 
El ingreso de datos finaliza cuando se ingresa 999. 
Determinar la cantidad de números pares 
y la suma de impares ingresados.
"""

def ingresar_numero() -> int:
    while True:
        try:
            return int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un valor valido!")

def es_par(numero: int) -> bool:
    return numero % 2 == 0

def main() -> None:
    a = ingresar_numero()

    if a != 999:
        if es_par(a):
            print(f"{a} es par")
        else:
            print(f"{a} NO es par")

if __name__ == "__main__":
    main()
    