"""
Ejercicio Nro 12
Realizar un programa donde se ingrese repetidamente números, 
determinar si los números son pares. 
El ingreso finaliza cuando el número es impar. 
Use la sentencia break para salir del ciclo. 
Al final mostrar el promedio de los números pares ingresados.
"""
from typing import Optional

def ingresar_numero() -> int:
    while True:
        try:
            return int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un valor valido!")

def es_par(numero: int) -> bool:
    return numero % 2 == 0


# Esta función devuelve un float si se puede calcular el promedio.
# Si no hay números pares (contador == 0), devuelve None.
# Usamos 'Optional[float]' para indicar que el resultado puede ser un float o None.
def determinar_promedio(contador: int, acumulador) -> Optional[float]:
    if contador == 0:
        return None
    return acumulador / contador
    

def main() -> None:
    contador_pares = 0
    acumulador_pares = 0


    while True:
        numero = ingresar_numero()
        if not es_par(numero):
            break
        contador_pares += 1
        acumulador_pares += numero

    promedio = determinar_promedio(contador_pares, acumulador_pares)
    if promedio is not None:
        print(f"El promedio de los numeros ingresados es: {promedio}")
    else:
        print("No se puede calcular el promedio! No hay numeros pares")

if __name__ == "__main__":
    main()

    