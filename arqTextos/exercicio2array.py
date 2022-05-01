lista=[]
i=0

print("Informe quatro numeros abaixo:\n")
while i<4:
    lista.append(float(input("Informe um valor numerico: ")))
    i+=1
print("")

tipo=input("Informe em qual ordem voce deseja colocar a lista,\n1-CRESCENTE ou 2-DECRESCENTE: ")

if tipo=='1':
    lista.sort()
else:
    lista.reverse()

print(lista)

