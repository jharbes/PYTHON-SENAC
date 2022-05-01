class Conta():

    def __init__(self, nome, tipo, saldo):
        """Inicializaos atributos name e age"""

        self.nome = nome
        self.tipo = tipo
        self.saldo = saldo

    def exibirSaldo(self):
        print(self.nome + " - ", self.saldo)

        print("------------------------------")

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self,valor):
        if self.saldo>=valor:
            self.saldo=self.saldo-valor
        else:
            print("Transacao nao autorizada")


c1 = Conta("Ana", "C", 1000)

c1.exibirSaldo()

c1.depositar(500)

c1.exibirSaldo()

c1.sacar(2000)

c1.exibirSaldo()