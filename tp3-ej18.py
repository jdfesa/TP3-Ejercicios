"""
Ejercicio Nro 18
Realizar un programa que permita ingresar 6 números, 
contar la cantidad de números negativos y cero, 
y acumular los números positivos. 
Mostrar el promedio de los números positivos 
y también mostrar la cantidad de negativos iguales a -5.
"""
def ingresar_numero() -> int:
    while True:
        try:
            return int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un valor valido!")

def es_numero_negativo(numero: int) -> bool:
    return numero < 0

def es_numero_cero(numero: int) -> bool:
    return numero == 0

def es_numero_positivo(numero: int) -> bool:
    return numero > 0

def calcular_promedio(suma: int, cantidad: int) -> float:
   if cantidad == 0:
       return 0.0
   return suma / cantidad

def main() -> None:
    veces = 6
    contador_negativos = 0
    cont_neg_igual_a_menos_cinco = 0
    contador_ceros = 0
    suma_positivos = 0
    contador_positivos = 0

    for _ in range(veces):
        numero = ingresar_numero()
        if es_numero_negativo(numero):
            contador_negativos += 1
            if numero == -5:
                cont_neg_igual_a_menos_cinco += 1
        elif es_numero_cero(numero):
                contador_ceros += 1
        elif es_numero_positivo(numero):
            suma_positivos += numero
            contador_positivos += 1
    
    promedio_positivos = calcular_promedio(suma_positivos, contador_positivos)
    
    print(f"\nCantidad de números negativos: {contador_negativos}")
    print(f"Cantidad de ceros: {contador_ceros}")
    print(f"Suma de positivos: {suma_positivos}")
    print(f"Promedio de positivos: {promedio_positivos:.2f}")
    print(f"Cantidad de negativos iguales a -5: {cont_neg_igual_a_menos_cinco}")

    
if __name__ == "__main__":
    main()