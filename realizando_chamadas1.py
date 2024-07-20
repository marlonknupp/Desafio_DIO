# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    # Método para permitir que um usuário faça uma chamada telefônica
    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        if custo <= self.plano.verificar_saldo():
            self.plano.deduzir_saldo(custo)
            saldo_restante = self.plano.verificar_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

# Classe Plano, representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    # Método para verificar saldo e retornar o saldo atual
    def verificar_saldo(self):
        return self.saldo

    # Método para calcular o custo de uma chamada (supondo o custo de $0.10 por minuto)
    def custo_chamada(self, duracao):
        return duracao * 0.10

    # Método para deduzir o valor do saldo do plano
    def deduzir_saldo(self, valor):
        self.saldo -= valor

# Classe UsuarioPrePago, herda de UsuarioTelefone e representa um usuário pré-pago:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Criando objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)

# Recebendo informações para simular uma chamada telefônica:
destinatario = input()
duracao = int(input())

# Chamando o método fazer_chamada do objeto usuario_pre_pago e imprimindo o resultado:
resultado_chamada = usuario_pre_pago.fazer_chamada(destinatario, duracao)
print(resultado_chamada)