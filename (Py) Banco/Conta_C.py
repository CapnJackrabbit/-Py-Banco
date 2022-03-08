class Conta:
    def __init__(self, saldo_inicial):
        self.set_saldo(saldo_inicial)

    def set_saldo(self, saldo_inicial):
        self._saldo = saldo_inicial

    def deposito (self, valor_deposito):
        if valor_deposito <= 0:
            print("Nao e possivel depositar valores nulos ou negativos\n")
        else:
            self._saldo += valor_deposito
    def saque (self, valor_saque):
        if valor_saque <= 0:
            print ('Nao e possivel sacar valores nulos ou negativos\n')
        elif valor_saque > self._saldo:
            print ('Saldo insufuciente\n')
        else:
            self._saldo -= valor_saque

    def get_saldo(self):
        return self._saldo