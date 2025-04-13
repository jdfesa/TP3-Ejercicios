"""
Ejercicio Nro 15
Considerando que el producto entero dos números enteros positivos,
a y b, puede expresarse como la suma sucesiva 
de a tantas veces como indique b, 
diseñe un algoritmo que 
calcule el producto entre a y b mediante sumas sucesivas.
"""

def ingresar_numero() -> int:
    while True:
        try:
            return int(input("Ingrese un numero: "))
        except ValueError:
            print("Ingrese valores validos!")

def producto(a: int, b: int) -> int:
    suma = 0
    for _ in range(0, b):
        suma+= a
    return suma

def main() -> None:
    numero_a = ingresar_numero()
    numero_b = ingresar_numero()


    print(f"{numero_a} * {numero_b} es: {producto(numero_a, numero_b)}")

if __name__ == "__main__":
    main()

