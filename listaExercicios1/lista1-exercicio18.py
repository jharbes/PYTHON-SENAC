# Conferir se eh possivel votar

ano=input("Informe o ano de nascimento da pessoa com quatro digitos: ")
ano=int(ano)
ano1=input("Informe o ano atual com quatro digitos: ")
ano1=int(ano1)

if (ano1-ano)>=16:
    print("Pessoa habilitada para votar")
else:
    print("Pessoa NÃO habilitada para votar")