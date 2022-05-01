mesa=[0,0,0]
pedido=[20,30,40]
x=1

while x!='3':
    print("SISTEMA DE PEDIDOS\n")
    print("1- LANCAR PEDIDO")
    print("2- FECHAR CONTA")
    print("3- ENCERRAR APLICATIVO")
    x=input("Escolha a opcao: ")
    if x=='1':
        m=int(input("pra qual mesa eh o pedido? "))
        p=int(input("qual o numero do pedido? "))
        mesa[m]=mesa[m]+pedido[p]
    elif x=='2':
        m=int(input("Deseja encerrar a conta de que mesa: "))
        print("O valor total da conta (com a taxa de servico) eh de R$",mesa[m]*1.1)
        n=int(input("Deseja que seja dividido pra quantos pagantes: "))
        print("O valor por pessoa eh de R$",mesa[m]*1.1/n)
        mesa[m]=0
        print("Conta da mesa",m,"zerada.")
    else:
        break;


