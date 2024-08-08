lista_precios_semana = [50, 20, 21, 90, 50, 60, 87]
dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

# no pythonico
# for i in [5, 6]:
#     print(f"{dias_semana[i]}: {lista_precios_semana[i] * 0.5}")

# pythonica
# for dia, precio in zip(dias_semana[5:], lista_precios_semana[5:]):
#     print(dia, precio)

dias_2 = []

for i, dia in enumerate(dias_semana):
    if i % 2 == 0:
        dias_2.append(dia)

dias_3 = [dia for i, dia in enumerate(dias_semana) if i % 2 == 0]
print(dias_2)

precios_2 = []

for precio in lista_precios_semana:
    if precio > 50:
        precios_2.append(precio)

print(precios_2)

precios_3= [precio for precio in lista_precios_semana if precio > 50]
print(precios_3)