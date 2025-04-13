"""
Ejercicio Nro 13
Realizar un programa que determine el máximo de una serie de números enteros
ingresados por el usuario. 
El ingreso finaliza a pedido del usuario.
"""

def ingresar_numero() -> int:
    while True:
        try:
            return int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un valor valido!")

def determinar_mayor(numero_actual: int, mayor: int) -> int:
    if numero_actual > mayor:
        return numero_actual
    return mayor

def main() -> None:
    
    mayor = None

    while True:
        numero = ingresar_numero()

        # Si es el primer número ingresado, lo tomamos como el mayor inicial.
        if mayor is None:
            mayor = numero
        else:
         # Comparamos con el mayor actual y actualizamos si es necesario.
            mayor = determinar_mayor(numero, mayor)

        if input("Desea ingresar otro numero S/N: ").upper() != 'S':
            break

    print(f"El mayor es: {mayor}")


if __name__ == "__main__":
    main()