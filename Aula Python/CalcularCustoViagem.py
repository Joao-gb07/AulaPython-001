nome = input("DIgite seu nome: ")
distancia = float(input("Informe a distancia da viagem (em km): "))
velocidade = float(input("Informe a velocidade média (em km/h): "))
consumo = float(input("Informe o consumo do veículo (km por litro): "))
preco_combustivel = float(input("Informe o preço do litro do combustível (R$): "))

#Processamento
tempo = distancia / velocidade
litros = distancia / consumo
custo = litros * preco_combustivel

#Sáida dos Dados

print("\nRelatório de Viagem:")
print(f"Passageiro: {nome}")
print(f"Distancia: {distancia} km")
print(f"Velocidade media: {velocidade:.1f} km/h")
print(f"Duração estimada: {tempo:.2f} horas")
print(f"COmbustivel necesario: {litros:.2f} litros")
print(f"Custo estimado da viagem: R$ {custo:.2f}")