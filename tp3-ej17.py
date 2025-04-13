"""
Ejercicio Nro 17
Tomando  el  algoritmo  del  punto  8  para  determinar  
si  un  número  es  primo,  
se  ingresan repetidamente números, 
lo que se pide es que determinar la cantidad de números primos 
que fueron ingresados y la suma de los números que no fueron primos. 
El ingreso de datos finaliza cuando la cantidad de números primos 
sea superior a 7.
"""

def ingresar_numero() -> int:
    while True:
        try:
            return int(input("Ingrese numero: "))
        except ValueError:
            print("Debe ingresar un valor valido!")

def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    
    for i in range(2, (int)(numero/2) + 1):
        if numero % i == 0:
            return False
    return True

def main() -> None:
    contador_primos = 0
    suma_no_primos = 0

    # Se corta cuando la cantidad de primos es superior a 7

    while contador_primos <= 7:
        numero = ingresar_numero()
        
        if es_primo(numero):
            contador_primos += 1
        else:
            suma_no_primos += numero

    print(f"Cantidad primos: {contador_primos}. Suma de no primos: {suma_no_primos}")

if __name__ == "__main__":
    main()
