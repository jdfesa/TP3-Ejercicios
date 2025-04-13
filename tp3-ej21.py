"""
Ejercicio Nro 21
Realizar un programa que dibuje un triángulo invertido 
con altura mínima de 5 líneas. 
La salida debería tener la forma:
Altura = 5
    +***+
    +**+
    +*+
    ++
    +
Altura = 10
    +********+ 
    +*******+ 
    +******+ 
    +*****+ 
    +****+
    +***+
    +**+ 
    +*+ 
    ++
    +
"""

def ingresar_numero() -> int:
    while True:
        try:
            entrada = int(input("Ingrese numero (minimo 5): "))
            if entrada < 5:
                print("La entrada debe ser mayor o igual 5")
            else: 
                return entrada
        except ValueError:
            print("Debe ingresar un valor valido!")

def dibujar_triangulo(altura: int) -> None: 
    print(f"Altura = {altura}")
    for i in range(altura, 0, -1):  # Desde altura hasta 1 (decreciendo)
        linea = "+" + ("*" * i) + "+"
        print(linea)
    
def main() -> None:
    altura = ingresar_numero()
    dibujar_triangulo(altura)

if __name__ == "__main__":
    main()

