nome = input(str("Digite seu nome: "))
print(f"Olá {nome} !")

nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - nascimento

if idade >= 18:
    print(f"Acesso Liberado {nome}, você é maior de idade")
else:
    print(f"Acesso negado {nome}, você é menor de idade")