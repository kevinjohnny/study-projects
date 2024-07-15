from abc import ABC, abstractmethod
from datetime import date, datetime

class Cliente:
    #Privates: endereço Str; contas list
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
        
    def realizar_operacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)
        
    def __str__(self):
       return f'Endereco: {self._endereco} - contas vinculadas: {len([conta for conta in self._contas])}'
       
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(endereco)
    
class Conta:
    #Private: saldo(float); numero(int); agencia(str); cliente: CLiente(classe); historico: Historico
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
        
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
            
    def mostrar_saldo(self):
        print(self.saldo)
    
    def __str__(self):
        return f'Cliente: {self._cliente} - Agencia: {self._agencia} - Numero {self._numero}'
    
    def sacar(self, valor):
        if valor > self._saldo:
            print("Valor excede saldo")
        elif valor > 0:
            self._saldo -= valor
            print(f"\nSaque de {valor} realizado com sucesso!")
            return True
        else:
            print("Operacao falhou! Insira um valor válido!")
        return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\nDepósito de {valor} realizado com sucesso!")            
            return True
        else:
            print("\nValor de depósito inválido!")
            return False

class ContaCorrente(Conta):
    LIMITE = 500
    LIMITE_SAQUES = 3
    
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        
    def sacar(self, valor):
        limite_saque = ContaCorrente.LIMITE_SAQUES
        limite = ContaCorrente.LIMITE
        saques = len([transacao for transacao in self.historico.transacoes if transacao["transacao"] == "Saque"])
        
        if saques > limite_saque:
            print("Limite de saques excedido!")
        elif valor > limite:
            print("Valor excede o limite por transação!")
        
        else:
            super().sacar(valor)   
            return True  
        
        return False     
    
    def __str__(self):
        return f'Agencia {self._agencia}\nConta Corrente {self._numero}\nTitular {self._cliente.nome}'
        
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass
        
class Deposito(Transacao):
    
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.depositar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.sacar()
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Historico():
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
        
    def adicionar_transacao(self, transacao):
        self._transacoes.append({"transacao": transacao.__class__.__name__,
                               "valor": transacao.valor})#,
                               #"data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")})

pessoa = PessoaFisica("06721", "Antonio", "12/3/1987", "Rua Escandinava")
conta = ContaCorrente("Antonio", 1)
pessoa.adicionar_conta(conta)
print(pessoa)
pessoa.realizar_operacao(conta, Deposito(10))
print(conta._saldo)
conta.depositar(20)
conta.mostrar_saldo()
print(pessoa._contas)