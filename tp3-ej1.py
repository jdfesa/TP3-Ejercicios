"""
Ejercicio Nro 1
Realizar un programa que muestre la frase “Curso Python” 7 veces.
"""

def ingresar_frase() -> str:
    return "Curso Python"

def main():
    print(ingresar_frase())

if __name__ == "__main__":
    veces = 0
    while(veces < 7):
        main()
        veces += 1