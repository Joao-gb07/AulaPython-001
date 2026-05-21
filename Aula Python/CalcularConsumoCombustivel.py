distancia_total = float(input("Digite a distância total percorrida em km: "))
consumo_combustivel = float(input("Digite o ttoal de combustível gasto em L: "))

#Calcular Consumo Médica Combustível km/l

consumo_medio = distancia_total / consumo_combustivel

if consumo_medio < 10:
    print(f"Seu consumo médio foi de {consumo_medio} km/l, Consumo Alto")
else:
    print(f"Seu consumo médio foi de {consumo_medio} km/l, Consumo dentro do esperado")