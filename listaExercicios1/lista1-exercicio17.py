# Calculo de aprovacao

n1=input("Informe o valor da primeira nota: ")
n1=float(n1)
n2=input("Informe o valor da segunda nota: ")
n2=float(n2)

media=(n1+n2)/2

if media>=6:
    print("Aluno aprovado com media",media)
else:
    print("Aluno reprovado com media",media)