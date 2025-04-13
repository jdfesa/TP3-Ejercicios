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
    while True:
        try:
            return int(input("Ingrese numero: "))
        except ValueError:
            print("Debe ingresar un numero valido!")

def reescribir_a_caracter(numero: int) -> chr:
    if numero == 1:
        return 'I'
    elif numero == 2:
        return 'Z'
    elif numero == 3:
        return 'E'
    elif numero == 4:
        return 'A'
    elif numero == 5:
        return 'S'
    elif numero == 6:
        return 'G'
    elif numero == 7:
        return 'T'
    elif numero == 8:
        return 'B'
    elif numero == 9:
        return 'g'
    elif numero == 0:
        return 'O'
    
def extraer_digito(numero: int) -> int:
    return numero % 10

def actualizar_numero(numero: int) -> int:
    return numero / 10

def main() -> None:
    numero = ingresar_numero()
    palabra = ""
    while numero != 83457:
        while numero != 0:
            digito = extraer_digito(numero)
            caracter = reescribir_a_caracter(digito)
            numero = actualizar_numero(numero)
            palabra += caracter
    print(f"La palabra equivalente es: {palabra}")

if __name__ == "__main__":
    main()

