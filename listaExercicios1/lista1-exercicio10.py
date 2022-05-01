# Custo de um carro

custo=input("Informe o valor de custo do carro: ")
custo=float(custo)

distribuidor=custo*0.28
impostos=custo*0.45

print("O custo final ao consumidor eh de",custo+distribuidor+impostos)
