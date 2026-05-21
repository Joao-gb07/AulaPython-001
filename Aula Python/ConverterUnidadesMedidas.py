distancia_km = float(input("Digite uma distância em km: "))

calcular_jardas = (distancia_km * 1093.61)
calcular_milhas = (distancia_km / 1.60934)

print(f"{distancia_km:.2f} km convertido em Jardas é = {calcular_jardas:.2f} yd")
print(f"{distancia_km:.2f} km convertido em Milhas é = {calcular_milhas:.2f} Milhas")