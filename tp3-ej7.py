"""
Ejercicio Nro 7
Realizar un programa que permita ingresar una frase 
y la cantidad de veces que desea mostrar la frase. 
Y mostrarla por pantalla esa cantidad de veces. 
La frase debe mostrarse con cada palabra 
empezando en mayúsculas para las iteraciones pares 
(considere que la primera iteración es la 1).
"""

def ingresar_frase() -> str:
    while True:
        try: 
            return input("Ingrese una frase: ")
        except ValueError:
            print("Ingrese un valor correcto!")

def ingresar_cantidad_de_repeticiones() -> int:
    while True:
        try: 
            return int(input("Ingrese cantidad de repeticiones: "))
        except ValueError:
            print("Debe ingresar un valor valido!")

def main() -> None:
    frase = ingresar_frase()
    veces = ingresar_cantidad_de_repeticiones()

    for i in range(1, veces+1):
        # Si el número de repetición es par, aplicar .title() 
        # para poner en mayúscula la primera letra de cada palabra.
        if i % 2 == 0:
            print(frase.title())
        else:
            # Si es impar, imprimir la frase tal como fue ingresada.
            print(frase)


if __name__ == "__main__":
    main()


