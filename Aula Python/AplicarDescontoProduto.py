valor_produto = float(input("Digite o valor do produto R$ "))

calculo_desconto1 = valor_produto * 0.10
calculo_desconto2 = valor_produto * 0.05

if (valor_produto >100):
    print(f"Você ganhou um desconto de R$ {calculo_desconto1} e irá pagar R$ {valor_produto - calculo_desconto1}")
else:
    print(f"Você ganhou um desconto de R$ {calculo_desconto2} e irá pagar R$ {valor_produto - calculo_desconto2}")
