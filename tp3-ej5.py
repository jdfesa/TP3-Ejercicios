"""
Ejercicio Nro 5
Realizar un programa que permita ingresar letras 
y por cada una contar las ocurrencias de las letras 
del abecedario en mayúsculas, 
también contar las letras minúsculas y dígitos. 
El ciclo finaliza al ingresar un espacio. 
Al finalizar muestre el total de letras ingresadas, 
en mayúsculas, en minúsculas, la cantidad de vocales 
que se ingresaron en mayúscula y minúscula, 
la cantidad de letras ‘J’ ingresadas 
y la cantidad de dígitos.
"""

def crear_contadores() -> dict:
    """
    Inicializa y devuelve un diccionario con todos los contadores necesarios.
    """

    # Esta línea crea un diccionario con las letras de la A a la Z como claves
    # y 0 como valor inicial para cada una de ellas.
    # chr(letra) convierte el número (código ASCII) en letra.
    # range(ord('A'), ord('Z') + 1) genera los códigos ASCII desde 'A' hasta 'Z'.
    ocurrencias_mayusculas = {chr(letra): 0 for letra in range(ord('A'), ord('Z') + 1)}

    return {
        "mayusculas": 0,
        "minusculas": 0,
        "digitos": 0,
        "vocales_mayus": 0,
        "vocales_minus": 0,
        "cantidad_j": 0,
        "ocurrencias_mayusculas": ocurrencias_mayusculas
    }

def ingresar_letra() -> str:
    while True:
        letra = input("Ingrese una letra (ESPACIO para finalizar): ")
        if len(letra) == 1:
            return letra
        print("Debe ingresar un solo caracter.")


def es_vocal(letra: str) -> bool:
    """
    Retorna True si la letra es una vocal.
    """
    return letra.lower() in "aeiou"

def actualizar_contadores(letra: str, contadores: dict) -> None:
    """
    Recibe una letra y el diccionario de contadores.
    Actualiza los contadores según la letra ingresada.
    """

    if letra.isupper():
        contadores["mayusculas"] += 1
        contadores["ocurrencias_mayusculas"][letra] += 1
        if es_vocal(letra):
            contadores["vocales_mayus"] += 1

    elif letra.islower():
        contadores["minusculas"] += 1
        if es_vocal(letra):
            contadores["vocales_minus"] += 1

    elif letra.isdigit():
        contadores["digitos"] += 1

    if letra.upper() == 'J':
        contadores["cantidad_j"] += 1

def mostrar_resultados(contadores: dict) -> None:
    """
    Imprime todos los resultados almacenados en los contadores.
    """
    print(f"Total letras mayúsculas: {contadores['mayusculas']}")
    print(f"Total letras minúsculas: {contadores['minusculas']}")
    print(f"Total dígitos: {contadores['digitos']}")
    print(f"Vocales mayúsculas: {contadores['vocales_mayus']}")
    print(f"Vocales minúsculas: {contadores['vocales_minus']}")
    print(f"Cantidad de letras 'J': {contadores['cantidad_j']}")
    print("\nOcurrencias de letras mayúsculas:")
    
    # Recorremos el diccionario de ocurrencias. Cada par clave-valor (letra y su cantidad) se separa automáticamente usando .items()
    
    for letra, cantidad in contadores["ocurrencias_mayusculas"].items():
        print(f"{letra}: {cantidad}")

def main() -> None:
    contadores = crear_contadores()

    while True:
        letra = ingresar_letra()
        if letra == " ":
            break
        actualizar_contadores(letra, contadores)

    mostrar_resultados(contadores)

if __name__ == "__main__":
    main()


    