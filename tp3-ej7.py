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
        # Si la iteracion es para, usamos .title()
        # para poner la primera letra de cada palabra
        # en mayuscula
        if i % 2 == 0:
            print(frase.title())
        else:
            print(frase)


if __name__ == "__main__":
    main()


