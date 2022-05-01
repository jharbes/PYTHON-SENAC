x=1
candidato=['','','']
votacao=[0,0,0]

while x!='4':
    print("SISTEMA DE VOTACAO\n")
    print("1- LANCAR CANDIDATO")
    print("2- FAZER A VOTACAO")
    print("3- VER RESULTADO")
    print("4- FINALIZAR SISTEMA\n")
    x=input("Escolha a opcao: ")
    if x=='1':
        for i in range(0,3):
            # recebendo o nome dos candidatos
            print("\nDIGITE O NOME DO CANDIDATO DE NUMERO",i+1)
            candidato[i]=input("Nome: ")
    elif x=='2':
        # primeiro impedimos que sejam recebidos votos sem antes alimentar o nome dos candidatos
        if candidato[0]!='' or candidato[1]!='' or candidato[2]!='':
            print("\nSISTEMA DE VOTACAO INICIADA.\n")
            for i in range(0,40):
                print("INFORME O VOTO DE NUMERO",i+1)
                voto=input("Opcao 1, 2 ou 3: ")
                # abaixo impediremos que sejam recebidos votos diferentes de 1, 2 ou 3
                while voto!='1' and voto!='2' and voto!='3':
                    print("OPCAO INVALIDA!")
                    voto=input("INFORME APENAS UMA DAS TRES OPCOES (1, 2 OU 3): ")
                voto=int(voto)
                votacao[voto-1]+=1

        else:
            print("\nNOMES DOS CANDIDATOS NAO FORAM INSERIDOS DEVIDAMENTE,")
            print("FAVOR REUTILIZAR A OPCAO 1 ANTES DE PROCEDER.\n")
    elif x=='3':
        # abaixo o programa testa se ja foi feita a votacao antes de permitir ler os resultados
        if votacao[0]+votacao[1]+votacao[2]==0:
            print("\nVOTACAO NAO REALIZADA AINDA,\nPRIMEIRAMENTE UTILIZAR A OPCAO 2 POR FAVOR.\n")
        else:
            maximo=max(votacao)
            # aqui o programa testa se houve empate dos primeiros lugares e manda refazer a votacao
            if (votacao[0]==maximo and votacao[1]==maximo) or (votacao[0]==maximo and votacao[2]==maximo) or (votacao[1]==maximo and votacao[2]==maximo):
                print("\nHOUVE EMPATE NO RESULTADO DE 1o LUGAR, FAVOR REFAZER VOTACAO.\n")
            else:
                print("\nSEGUE O RESULTADO FINAL DA VOTACAO:\n")
                for i in range(0,3):
                    print("O CANDIDATO",i+1,", SENHOR(A)",candidato[i].title(),",OBTEVE UM TOTAL DE",votacao[i],"VOTOS.")
                    print("O PERCENTUAL DE VOTOS DO CANDIDATO",i+1,"EM RELACAO AO TOTAL "
                           "DE VOTOS FOI DE",round(votacao[i]/(votacao[0]+votacao[1]+votacao[2])*100,2),"%\n")
                print("O CANDIDATO VENCEDOR FOI O DE NUMERO",votacao.index(max(votacao))+1)
                print("PARABENS SENHOR(A)",candidato[votacao.index(max(votacao))].title(),", GRANDE VITORIA!\n")
    elif x=='4':
        print("\nSISTEMA FINALIZADO")
        break;
    else:
        print("\nOPCAO INVALIDA, FAVOR TENTAR NOVAMENTE\n")