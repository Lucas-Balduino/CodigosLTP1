from abc import ABC, abstractmethod

'''
    Criar um sistema de simulação bancária onde diferentes tipos de contas compartilham algumas operações comuns,mas também têm regras específicas. 
    Defina uma classe abstrata ContaBancaria com métodos abstratos para depositar, sacar e calcular saldo. 
    Crie duas subclasses concretas, ContaCorrente e ContaPoupanca. 
    A ContaCorrente deve permitir um saldo negativo até um certo limite (cheque especial). 
    A ContaPoupanca não deve permitir saldo negativo e deve calcular juros sobre o saldo atual.
    Implementar métodos para exibir informações da conta.
    As contas devem ter atributos como número da conta, titular e saldo.
    A função sacar de ContaPoupanca deve recusar a operação se o saldo ficar negativo.
'''

class ContaBancaria():
    def __init__(self,codigo, titular, saldo):
        self.codigo = codigo
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod
    def sacar(self):
        pass

    @abstractmethod
    def calcularSaldo(self):
        pass

    def informacoes(self):
        return f"Dados da Conta: Codigo-{self.codigo}, Titular-{self.titular}, Saldo-{self.saldo}"
    
class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, saldo = 0, limiteChequeEspecial = 500):
        super().__init__(numero, titular, saldo)
        self.limiteChequeEspecial = limiteChequeEspecial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor:.2f} realizado com sucesso!")
    
    def sacar(self, valor):
        if valor > 0 and self.saldo - valor >= -self.limiteChequeEspecial:
            self.saldo -= valor
            print(f"Saque de {valor:.2f} realizado com sucesso! Cheque Especial utilizado")
        elif valor > 0:
            self.saldo -= valor
            print(f"Saque de {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para saque, mesmo com cheque especial.")


    def calcularSaldo(self):
        return self.saldo

    def informacoes(self):
        return f"{super().informacoes()},Limite do Cheque Especial-{self.limiteChequeEspecial}"
    
class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular, saldo = 0, taxaJuros = 0.1):
        super().__init__(numero, titular, saldo)
        self.taxaJuros = taxaJuros

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para saque.")
    
    def calcularSaldo(self):
        self.saldo += self.saldo * self.taxaJuros
        return self.saldo
    
    def informacoes(self):
        return f"{super().informacoes()},Taxa de Juros-{self.taxaJuros}"

contaCorrente = ContaCorrente("12345-6","João Silva",1000,500)
contaPoupanca = ContaPoupanca("65432-1","Maria Oliveira",2000, 0.05)

# Operações na Conta Corrente
print(contaCorrente.informacoes())
contaCorrente.depositar(300)
contaCorrente.sacar(1500)  # Utiliza o cheque especial
print(contaCorrente.informacoes())

# Operações na Conta Poupança
print(contaPoupanca.informacoes())
contaPoupanca.depositar(500)
contaPoupanca.sacar(3000)  # Deve recusar o saque
contaPoupanca.calcularSaldo()
print(contaPoupanca.informacoes())
