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