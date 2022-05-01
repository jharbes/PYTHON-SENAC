
nome=input("Informe o nome do funcionario: ")
salario=float(input("Informe o valor bruto do salario do funcionario: "))
vt=float(input("Informe o custo de transporte com o funcionario: "))
print("")

if salario<=1212:
    inss=salario*0.075
elif salario>1212 and salario<=2427.35:
    inss=1212*0.075+(salario-1212)*0.09
elif salario>2427.35 and salario<=3641.03:
    inss=1212*0.075+(24247.35-1212)*0.09+(salario-2427.35)*0.12
elif salario>3641.03 and salario<=7087.22:
    inss=1212*0.075+(2427.35-1212)*0.09+(3641.03-2427.35)*0.12+(salario-3641.03)*0.14
else:
    inss=1212*0.075+(2427.35-1212)*0.09+(3641.03-2427.35)*0.12+(7087.22-3641.03)*0.14

if vt>salario*0.06:
    vt=salario*0.06

print("O valor descontado de vale transporte do",nome,"sera de R$",vt)
print("O valor descontado de inss do",nome,"sera de R$",inss)
print("O salario liquido do",nome,"sera de R$",salario-inss-vt)


