from random import randint

npensado=randint(1,20)
respostaserradas=['ERROUUUUUU!','Errou feio!, Errou rude!','Falhou miseravelmente!','Tenta de novo que de repente vai!','Errou, voce nao desiste?']

print("Pensei em um numero, qual eh este numero?")
acerto=False
x=0

while acerto==False:
    chute=int(input("Que numero eh esse? "))
    x+=1
    if chute>npensado:
        print(respostaserradas[randint(0,4)])
        print("O chute eh MAIOR que o numero pensado.\n")
    elif chute<npensado:
        print(respostaserradas[randint(0,4)])
        print("O chute eh MENOR que o numero pensado.\n")
    else:
        print("ACERTOU!\n")
        acerto=True

print("Voce tentou",x,"vezes")


