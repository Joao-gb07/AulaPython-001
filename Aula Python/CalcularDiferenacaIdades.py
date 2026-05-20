idade1 = int(input("Digite a idade de A: "))
idade2 = int(input("Digite a idade de B: "))

difenca = idade1 - idade2

if difenca < 0:
    difenca = difenca * -1

print(f"A diferença é {difenca} anos")