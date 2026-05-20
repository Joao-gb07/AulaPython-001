nome = input(str("Digite seu nome: "))
print(f"Olá {nome} !")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Acesso Liberado {nome}, você é maior de idade")
else:
    print(f"Acesso negado {nome}, você é menor de idade")