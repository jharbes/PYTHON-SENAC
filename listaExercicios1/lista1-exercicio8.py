# Percentual de votos

total=input("Informe o numero total de eleitores: ")
total=int(total)
validos=input("Informe o numero de votos validos: ")
validos=int(validos)
brancos=input("Informe o numero de votos brancos: ")
brancos=int(brancos)
nulos=input("Informe o numero de votos nulos: ")
nulos=int(nulos)

print("\n")
print("O percentual de votos validos em relacao ao total de votos eh:",(validos/total)*100)
print("O percentual de votos brancos em relacao ao total de votos eh:",(brancos/total)*100)
print("O percentual de votos nulos em relacao ao total de votos eh:",(nulos/total)*100)