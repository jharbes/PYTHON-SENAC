# Calculo de remuneracao do vendedor

carros=input("Informe o total de numero de carros vendidos: ")
carros=int(carros)
vendas=input("Informe o valor total de vendas deste vendedor: ")
vendas=float(vendas)
salfixo=input("Informe o valor do salario fixo desse vendedor: ")
salfixo=float(salfixo)
porcarro=input("Informe o valor recebido por carro vendido: ")
porcarro=float(porcarro)

print("O salario total desse vendedor sera de",salfixo+carros*porcarro+vendas*0.05)

