## Escrevendo funcao display message

def display_message():
    print("Estou aprendendo funcoes em python\n")

display_message()

def favorite_book(title):
    print("Um dos meus livros favoritos eh",title)

title='alice no pais das maravilhas'

favorite_book(title)
print("\n")
favorite_book('Asas')

## Exercicio 8.3

def makeshirt(tamanho,mensagem):
    print("O tamanho da camiseta eh " + tamanho + " e a mensagem eh " + mensagem)

makeshirt('M','Cool T-Shirt')
makeshirt(mensagem='Cool T-Shirt',tamanho='M')
print("\n")

## Exercicio 8.4

def makeshirt(tamanho='G',mensagem='Eu amo Python'):
    print("O tamanho da camiseta eh " + tamanho + " e a mensagem eh " + mensagem)

makeshirt()
makeshirt('M')
makeshirt(mensagem='Cool T-Shirt')
print('\n')

## Exercicio 8.5

def describe_city(cidade,pais='islandia'):
    print(cidade.title() + " esta localizada na " + pais.title())

describe_city('reykjavik')
describe_city('kopavogur')
describe_city('paris','franca')