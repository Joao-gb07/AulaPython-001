nome = input("Digite seu nome: ")

nota1 = float(input("Digite sua 1ª nota: "))
nota2 = float(input("Digite sua 2ª nota: "))
nota3 = float(input("Digite sua 3ª nota: "))

mediaPonderada = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 4

if (mediaPonderada >= 6):
    print(f"Parabéns {nome}! Você foi aprovado(a), sua média foi: {mediaPonderada}")
else:
    print(f"{nome}! Você foi reprovado(a), sua média foi: {mediaPonderada}")


