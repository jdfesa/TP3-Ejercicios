"""
Ejercicio Nro 16
Realizar un programa que permita ingresar números repetidamente, 
determinar el máximo de esos valores. 
El algoritmo termina cuando se ingresa un 10, 
utilice para terminar la repetición una interrupción con break.
"""

def ingresar_numero() -> int:
    while True:
        try:
            return int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un valor valido!")

def determinar_maximo(actual: int, maximo: int) -> int:
    if actual > maximo:
        return actual
    return maximo

def main() -> None:
    numero = ingresar_numero()
    maximo = numero
    
    while True:
        numero = ingresar_numero()
        if numero == 10:
            break
        maximo = determinar_maximo(numero, maximo)  

    print(f"El numero maximo es: {maximo}")
if __name__ == "__main__":
    main()

