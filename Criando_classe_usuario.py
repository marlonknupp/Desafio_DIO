# TODO: Crie uma classe UsuarioTelefone. 
class UsuarioTelefone:
# TODO: Defina um método especial init, que é o contrutor da classe
# O método init, irá inicializar os atributos da classe: nome, numero e plano
 def __init__(self,nome,numero,plano):
    self._nome = nome
    self._numero = numero
    self._plano = plano 
#TODO: Aplique o conceito de encapsulamento, onde os atributos serao encapsulados dentro da clase.
 def nome_usuario(self,nome):
   self._nome = nome
 def numero_usuario(self, numero):
   self._numero = numero
 def plano_usuario(self, plano):
   self._plano = plano

# A classe UsuarioTelefone define um método especial str, que retorna uma representaçao em string do objeto.
 def __str__ (self):
   return f"Usuário {self._nome} criado com sucesso."
 
 # Entrada:
nome = input()
numero = input()
plano = input()
#TODO: Crie um nome objeto Usuariotelefone com os dados fornecidos:
usuario = UsuarioTelefone(nome = nome, numero = numero, plano = plano)
print (usuario)


#DIO -----