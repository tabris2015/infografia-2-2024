import random

def mi_funcion(a, b, c):
    acumulado = a + b + c
    promedio = acumulado / 3

    return (acumulado, promedio)

dodge_prob = 0.1

iteraciones = 100
contador = 0
for i in range(iteraciones):
    if random.random() < dodge_prob:
        print("esquiva")
        contador += 1
    else:
        print("ouch")

print(f"{contador} / {iteraciones}")

