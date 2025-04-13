"""
Ejercicio Nro 10
Considerando que la potencia entre dos números enteros positivos, a y b, 
la potencia puede expresarse como el producto sucesivo 
de a tantas veces como lo indique b. 
Pida ingresar estos dos valores, 
y calcule la potencia con el algoritmo indicado.
"""

def ingresar_valores() -> tuple[int, int]:
    while True:
        try:
            a = int(input("Ingrese base: "))
            b = int(input("Ingrese exponente: "))
            return a, b
        except ValueError:
            print("Ingrese valores validos!")

def potencia(a: int, b: int) -> int:
    # 2^3 = 2 * 2 * 2
    pot = 1
    for _ in range(b):
        pot = pot * a
    return pot

def main() -> None:
    a, b = ingresar_valores()
    
    print(f"{a} elevado a {b} es igual a {potencia(a, b)}")

if __name__ == "__main__":
    main()



