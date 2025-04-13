"""
Ejercicio Nro 14
Realizar un programa donde se ingrese el nombre de un producto 
y el precio determine los precios máximo 
y mínimo de los productos ingresados. 
Considere que el ingreso de datos finaliza 
a petición del usuario si ingresa ‘s’ es un si y si ingresa ‘n’ es no.
"""


# En Python, tanto las tuplas como las listas usan corchetes [] 
# para acceder a sus elementos por índice.
# Pero la tupla se define con paréntesis () 
# o simplemente con comas al retornar (a, b).
# Las listas se definen con corchetes [].
# Por ejemplo: ("Pan", 120.5) es tupla, ["Pan", 120.5] es lista.
# Aunque use corchetes para acceder (ej: x[1]), 
# eso no significa que sea una lista.

# En Python, las tuplas se definen con () y son inmutables.
# Las listas se definen con [] y son mutables.
# Si devuelvo varios valores con "return a, b", es una tupla por defecto.
# Para confirmar el tipo de un objeto en tiempo de ejecución, uso type(objeto)





def ingresar_producto() -> tuple[str, float]:
    while True:
        try:
            producto = input("Ingrese nombre de producto: ")
            precio = float(input("Ingrese precio del producto: "))
            return producto, precio
        except ValueError:
            print("Ingrese valores validos!")

def determinar_precio_maximo(actual: tuple[str, float], maximo: tuple[str, float]) -> tuple[str, int]:
    if actual[1] > maximo[1]:
        return actual
    return maximo

def determina_precio_minimo(actual: tuple[str, float], minimo: tuple[str, float]) -> tuple[str, int]:
    if actual[1] < minimo[1]:
        return actual
    return minimo

def main() -> None:
    #Ingresamos el primer producto fuera del ciclo

    producto_actual = ingresar_producto()
    producto_max = producto_actual
    producto_min = producto_actual

    while True:
      respuesta = input("Desea ingresar otro producto (S/N): ").upper()
      if respuesta != 'S':
          break
      
      producto_actual = ingresar_producto()
      producto_max = determinar_precio_maximo(producto_actual, producto_max)
      producto_min = determina_precio_minimo(producto_actual, producto_min)

    print(f"Prod con precio maximo: {producto_max[0]}, ${producto_max[1]}")
    print(f"Prod con precio minimo: {producto_min[0]}, ${producto_min[1]}")

if __name__ == "__main__":
    main()
