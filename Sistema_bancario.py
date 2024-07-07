from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class cliente: 
    def __init__(self , endereco):
      self.endereco = endereco
      self.contas = []

    def realizar_transacao(self, conta, transacao):
      transacao.registrar(conta)

    def adicionar_conta(self, conta):
      self.contas.append(conta)

class PessoaFisica(cliente): 
    def __init__(self, nome , data_nascimento, cpf, endereco):
       super().__init__(endereco)
       self.nome = nome
       self.data_nascimento = data_nascimento
       self.cpf = cpf

class conta: 
    def __init__(self, numero , cliente):
       self._saldo = 0 
       self._numero = numero
       self._agencia = "0001"
       self._cliente = cliente
       self._historico = Historico ()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
       return cls(numero, cliente)
    @property
    def saldo(self):
       return self._numero
    
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
    
    def sacar(self, valor):
       saldo= self.saldo
       excedeu_saldo = valor > salvo

       if excedeu_saldo:
          print ("\n@@@ Operacao falhou! voce nao tem saldo suficiente!@@@")

       elif valor > 0:
          self._saldo -= valor
          print ("\n === Saque realizado com sucesso! =====")
          return True
       else: 
          print ("\n==== Operacao falhou! O valor informado é inválido. ====")
       return False

    def depositar (self, valor):
       if valor >0:
          self._saldo += valor
          print (" \n ==== Deposito realizado com sucesso =====")
       else:
          print ("\n ==== Operacao falhou! O valor informado é inválido. =====")
          return False
       
       return True
class ContaCorrente(conta):

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
       super().__init__(numero, cliente)
       self.limite = limite
       self.limite_saques = limite_saques
    
    def sacar(self, valor):
       numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "saque"])


       excedeu_limite = valor >self.limite
       excedeu_saques = numero_saques > self.limite_saques

       if excedeu_limite:
          print ('\n ====== Operacao falhou! O valor do saque excedeu o limite. =====')

       elif excedeu_saques:
          print ('\n ==== Operacao Falhou! numero máximo de saques excedido. =====')

       else :
          return super().sacar(valor)
       
       return False
    
    def __str__(self):
       return f"""\
         agencia:\t{self.agencia}
         C/C:\t\t{self.numero}
         titular:\t{self.cliente.nome}"""
               

class Historico:
    
    def __init__(self):
       self._transacoes = []

    @property
    def transacoes (self):
       return self._transacoes
    
    def adicionar_transacao(self, transacao):
       self._transacoes.append(
          {
             "tipo": transacao.__class__.__name__, 
             "valor": transacao.valor, 
             "data": datetime.now().strftime
             ("%d-%m-%Y %H:%M:%s"),
          }
       )

class transacao (ABC):
    @property
    @abstractproperty
    def valor(self):
       pass
    @abstractclassmethod
    def registrar (self,conta):
       pass
    

class Saque(transacao):
   def __init__(self, valor):
      self._valor = valor

   @property
   def valor(self):
      return self._valor
   
   def registrar(self, conta):
      sucesso_transacao = conta.sacar(self.valor)

      if sucesso_transacao:
         conta.historico.adicionar_transacao(self)

class Deposito (transacao):
   def __init__(self, valor ):
      self._valor = valor

   @property
   def valor (self):
      return self.valor
   
   def registrar(self, conta):
      sucesso_transacao = conta.depositar(self.valor)

      if sucesso_transacao:
         conta.historico.adicionar_transacao(self)


