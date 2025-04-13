"""
Ejercicio Nro 19
Realizar un programa que permita ingresar números, 
hasta que el número ingresado sea impar y este entre 1 y 10. 
Determinar el promedio de los números ingresados 
que no estuvieron entre 1 y 10.
"""
def ingresar_numero() -> int:
    while True:
        try:
            return int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un valor valido!")

def es_impar(numero: int) -> bool:
    return numero % 2 != 0

def calcular_promedio(suma: int, cantidad: int) -> float:
    if cantidad == 0:
        return 0.0
    return suma/cantidad

def main() -> None:
    
    contador = 0
    suma = 0
     
    while True:  
        numero = ingresar_numero() 

        if es_impar(numero) and (numero >= 1 and numero <= 10):
            break
        
        if not (numero >= 1 and numero <= 10):
            contador += 1
            suma += numero
        
    promedio = calcular_promedio(suma, contador)
    print(f"Promedio de los números fuera del rango 1-10: {promedio:.2f}")

if __name__ == "__main__":
    main()

          