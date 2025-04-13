"""
Ejercicio Nro 9
Realizar un programa que determine el mínimo de una serie 
de números enteros ingresados por el usuario. 
El ingreso finaliza cuando el valor introducido es 999.
"""

def ingresar_numero() -> int:
    while True: 
        try:
            return int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar valores validos!")

# Determina el menor entre el minimo actual y el nuevo numero ingresado
def determinar_minimo(minimo: int, numero: int) -> int:
    
    if numero < minimo:
        return numero
    return minimo

def main() -> None:
    a = ingresar_numero()

    # Asumo que el primer numero es el minimo inicial
    minimo = a

    while a != 999:
        minimo = determinar_minimo(minimo, a)
        a = ingresar_numero()

    print(f"El minimo numero ingresado es: {minimo}")

if __name__ == "__main__":
    main()

