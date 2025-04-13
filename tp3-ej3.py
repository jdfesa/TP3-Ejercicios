"""
Ejercicio Nro 3
Realizar un programa que calcule el promedio de los estudiantes, 
para ello se debe ingresar el apellido, nombre del estudiante y su nota. 
Considere que el ingreso finaliza a pedido del operador. 
Luego se debe mostrar el promedio 
seguido de la cantidad de personas que ingresaron su apellido todo en mayúsculas.
"""

def ingresar_datos_estudiantes() -> tuple[str, str, float]:
    while True:
        try:
            apellido = input("Ingrese apellido: ")
            nombre = input("Ingrese nombre: ")
            nota = float(input("Ingrese nota: "))

            return apellido, nombre, nota

        except ValueError:
            print("Debe ingresar valores validos!")

def es_apellido_mayusculas(apellido: str) -> bool:
    return apellido.isupper()

def calcular_promedio(suma: float, cantidad: int) -> float:
    if cantidad == 0:
        return 0
    return suma / cantidad

def mostrar_resultado(promedio: float, cantidad_apellidos_mayusculas : int) -> None:
    print(f"\nEl promedio de los alumnos es: {promedio}")
    print(f"La cantidad de apellidos en mayusculas es: {cantidad_apellidos_mayusculas}")


def main():
    suma_notas = 0
    cantidad_estudiantes = 0
    cantidad_apellidos_mayusculas = 0

    while True:
        apellido, nombre, nota = ingresar_datos_estudiantes()

        suma_notas += nota
        cantidad_estudiantes += 1

        if es_apellido_mayusculas(apellido):
            cantidad_apellidos_mayusculas += 1

        respuesta = input("Desea finalizar la carga?(S/N): ")
        if respuesta.upper() == 'S':
            break

    promedio = calcular_promedio(suma_notas, cantidad_estudiantes) 
    mostrar_resultado(promedio, cantidad_apellidos_mayusculas)


if __name__ == "__main__":
    main()

