# Calculo do valor de compra de macas

macas=input("Informe o numero de macas compradas: ")
macas=int(macas)

if macas<12:
    print("Valor da compra sera de R$",macas*1.3)
else:
    print("Valor da compra sera de R$",macas)