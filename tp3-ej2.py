"""
Ejercicio Nro 2
Realizar un programa que permita ingresar números enteros,
mostrar la suma de números pares, y la cantidad de números impares. 
El ingreso finaliza cuando el número es múltiplo de 5 (se incluye en el conteo).
"""

def ingresar_numero_entero() -> int:
    while True:
        try:
            return int(input("Ingrese un numero entero: "))
        except ValueError:
            print("Debe ingresar valores correctos!")

def determinar_paridad(numero: int) -> bool:
    return numero % 2 == 0


def main():
    suma_pares = 0
    cantidad_impares = 0


    while True:
        numero = ingresar_numero_entero()
        if determinar_paridad(numero):
            suma_pares += 1
        else:
            cantidad_impares += 1
        
        if numero % 5 == 0:
            break
    
    print(f"La suma de numeros pares es: {suma_pares}")
    print(f"La cantidad de numeros impares es: {cantidad_impares}")

if __name__ == "__main__":
    main()
