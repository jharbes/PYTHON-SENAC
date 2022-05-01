#entrada de dados utilizando o input("")
# mensagem=input("Digite o seu nome: ")

# ("Olá "+mensagem+" Bem vindo")

nome=input("Digite o nome do aluno: ")
n1=input("Digite a primeira nota: ")
n1=float(n1)
n2=input("Digite a segunda nota: ")
n2=float(n2)
n3=input("Digite a terceira nota: ")
n3=float(n3)
media=(n1+n2+n3)/3
if media>7:
    print(nome,"sua media foi",media,"e voce esta Aprovado\n\n")
else:
    print(nome,"sua media foi",media,"e voce esta reprovado\n\n")