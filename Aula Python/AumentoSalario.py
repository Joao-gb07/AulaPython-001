salario = float(input("Digite seu salário: "))

perceual_ajuste = float(input("Digite o percentual de aumento: (Ex: 20, 10 etc): "))

novo_salario = (salario * perceual_ajuste / 100) + salario

print(f"O valor de aumento foi de R$ {salario  * perceual_ajuste / 100:.2f}")

print(f"Seu novo salário com aumento foi de R$ {novo_salario:.2f}")