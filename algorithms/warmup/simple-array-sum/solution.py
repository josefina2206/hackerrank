import sys

def simple_array_sum(n, ar):
    # Completa esta función

n = int(input().strip()) # Tip: Esta variable almacena la cantidad de numeros.
ar = list(map(int, input().strip().split(' '))) # Tip: Esta variable almacena un arreglo que contiene los numeros a sumar.
result = simple_array_sum(n, ar)
print(result)

# Bonus: Obtienes puntos extras si eres capaz de explicar para que sirve:
# input() -> 
# strip() -> 
# int()   -> 
# map()   -> 
# split() -> 
# list()  -> 

