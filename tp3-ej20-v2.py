"""
Ejercicio Nro 20
Realizar un programa que acepte entrada de números. 
A cada número extraiga los dígitos, 
y luego reescriba el número original con la siguiente regla:
Número    Letra a usar
1           I
2           Z
3           E
4           A
5           S
6           G
7           T
8           B
9           g
0           O
Ejemplos:
Entrada    Salida
1211          IZII
795            TgS
8879          BBTg
El programa termina cuando se ingresa 
un número que forma la palabra BEAST. 
Nota: Trabaje el número como una cadena al extraer sus dígitos.
"""

def ingresar_numero() -> int:
    # Pide al usuario ingresar un número entero positivo
    while True:
        try:
            numero = int(input("Ingrese número: "))
            if numero >= 0:
                return numero
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Debe ingresar un número válido!")

def reescribir_digito(digito: int) -> str:
    # Mapea cada dígito a su correspondiente letra
    conversion = {
        1: 'I',
        2: 'Z',
        3: 'E',
        4: 'A',
        5: 'S',
        6: 'G',
        7: 'T',
        8: 'B',
        9: 'g',
        0: 'O'
    }
    return conversion.get(digito, '')

def convertir_a_palabra(numero: int) -> str:
    # Extrae dígitos desde el final y construye la palabra
    palabra = ""
    if numero == 0:
        return reescribir_digito(0)

    while numero > 0:
        digito = numero % 10             # Último dígito
        letra = reescribir_digito(digito)
        palabra = letra + palabra        # Agrega la letra al inicio
        numero //= 10                    # Elimina el último dígito

    return palabra

def main() -> None:
    while True:
        numero = ingresar_numero()
        palabra = convertir_a_palabra(numero)
        print(f"Traducción: {palabra}")
        
        if palabra == "BEAST":
            print("¡Se ingresó la palabra BEAST! Fin del programa.")
            break

if __name__ == "__main__":
    main()
