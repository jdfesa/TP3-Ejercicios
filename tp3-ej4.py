"""
Ejercicio Nro 4
Realizar un programa que permita ingresar 16 números, 
contar la cantidad de números negativos y cero, 
y concatenar los números positivos en una variable a mostrar.
Salida esperada
Negativos: 5
Ceros: 3
Positivos: 32615144
"""

def ingresar_numero() -> int:
    while True: 
        try:
            return int(input("Ingrese valor entero: "))
        except:
            print("Debe ingresar un valor valido!")

def es_negativo(numero: int) -> bool:
    return numero < 0 

def es_cero(numero: int) -> bool:
    return numero == 0

def es_positivo(numero: int) -> bool:
    return numero > 0


def main():
    negativos = 0
    ceros = 0
    concatenados = ""

# Repetimos el ingreso de números 16 veces, 
# no necesitamos usar la variable del for

    for _ in range(16): # Va de de 0 hasta 16-1 (en este caso)
        num = ingresar_numero()
        if es_negativo(num):
            negativos += 1
        elif es_cero(num):
            ceros += 1
        elif es_positivo(num):
            concatenados += str(num)
        
    print(f"Negativos: {negativos}")
    print(f"Ceros: {ceros}")
    print(f"Positivos: {concatenados}")

if __name__ == "__main__":
    main()

