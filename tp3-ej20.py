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

def ingresar_numero() -> str:
    while True:
        # Solicita al usuario que ingrese un número 
        # y se asegura de que sea válido (solo dígitos).
        try:
            entrada = ("Ingrese numero: ")
            if entrada.isdigit(): # Verifica que todos los caracteres sean dígitos (0–9)
                return entrada # Devuelve el número como cadena de texto
        except ValueError:
            print("Debe ingresar un numero valido!")

def reescribir_numero(numero: str) -> str:
    conversion = {
        '1': 'I',
        '2': 'Z',
        '3': 'E',
        '4': 'A',
        '5': 'S',
        '6': 'G',
        '7': 'T',
        '8': 'B',
        '9': 'g',
        '0': 'O'
    }
    palabra = "" # Acumulador para construir la palabra final
    
    
    # Recorremos cada carácter (dígito) de la cadena
    # Usamos .get(digito, '') para obtener el valor del diccionario:
    # Si el dígito está en el diccionario, devuelve la letra correspondiente
    # Si por alguna razón no está, devuelve una cadena vacía para evitar errores
    for digito in numero:
       # Dame la letra asociada a digito. Si no existe, devolvé una cadena vacía.
        palabra += conversion.get(digito, '')
    
    return palabra 
    
def main() -> None:
    while True:
        numero = ingresar_numero()  # Pide número como string
        palabra = reescribir_numero(numero)  # Traduce el número a palabra
        print(f"Traducción: {palabra}")
        
        # Si la palabra generada es "BEAST", se termina el programa
        if palabra == "BEAST":
            print("¡Se ingresó la palabra BEAST! Fin del programa.")
            break

if __name__ == "__main__":
    main()

