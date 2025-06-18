def calcular_consumo_medio(distancia_km, combustivel_litros):
    consumo_medio = round(distancia_km / combustivel_litros, 2)
    return consumo_medio

distancia_percorrida = 300
combustivel_gasto = 25

consumo_medio = calcular_consumo_medio(distancia_percorrida, combustivel_gasto)

print("Distância percorrida:", distancia_percorrida, "km")
print("Combustível gasto:", combustivel_gasto, "litros")
print("Consumo médio:", consumo_medio, "km/l")
