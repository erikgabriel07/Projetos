from os import system

class criarBancaria:
    def __init__(self, nome, endereco, num_tel, email, dt_nasc, numero=int, contaCorrente=True):
        while True:
            if '/' in dt_nasc or len(dt_nasc) < 8:
                break
            dt_nasc = input('Digite a data de nascimento do usuário no formato dd/mm/aa: ')

        self.informacoes_cliente = dict(nome=nome,
                                endereco=endereco,
                                num_tel=num_tel,
                                email=email,
                                dt_nasc=dt_nasc)

        self.informacoes_conta = dict(contaCorrente=contaCorrente,
                                      contaPoupanca=False,
                                      numero=numero,
                                      saldo=0.0)

        self.historico_transacoes = list()

        if self.informacoes_conta.get('contaCorrente') == False:
            self.informacoes_conta['contaPoupanca'] = True

    def editarConta(self):
        self.informacoes_cliente.__init__()
        while True:
            system('cls')
            print(f'ESCOLHA UM NÚMERO PARA EDITAR\n'
                  f'[1] Nome: {self.informacoes_cliente.get("nome")}\n'
                  f'[2] Endereço: {self.informacoes_cliente.get("endereco")}\n'
                  f'[3] Telefone: {self.informacoes_cliente.get("num_tel")}\n'
                  f'[4] Email: {self.informacoes_cliente.get("email")}\n'
                  f'[5] Nascimento: {self.informacoes_cliente.get("dt_nasc")}\n'
                  f'[0] Sair')
            user_input = input('>>> ').strip()[0]
            if user_input == '1':
                self.informacoes_cliente['nome'] = input('Digite o novo nome do usuário: ')
            if user_input == '2':
                self.informacoes_cliente['endereco'] = input('Digite o novo endereço do usuário: ')
            if user_input == '3':
                self.informacoes_cliente['num_tel'] = input('Digite o novo número do usuário: ')
            if user_input == '4':
                self.informacoes_cliente['email'] = input('Digite o novo email do usuário: ')
            if user_input == '5':
                self.informacoes_cliente['dt_nasc'] = input('Digite a nova data de nascimento do usuário: ')
            if user_input == '0':
                break

    def excluirConta(self):
        self.informacoes_cliente.clear()
        self.informacoes_conta.clear()
        self.historico_transacoes.clear()

    def depositar(self, valor_depositado):
        self.informacoes_conta['saldo'] = self.informacoes_conta['saldo'] + valor_depositado

    def sacar(self, valor_sacado):
        self.informacoes_conta['saldo'] = self.informacoes_conta['saldo'] - valor_sacado

    def transferir(self, conta_transferir=object, valor=float):
        while True:
            senha = input('Digite o número da sua conta: ')
            if senha == str(self.informacoes_conta['numero']):
                break
        if self.informacoes_conta['saldo'] > valor:
            conta_transferir.informacoes_conta['saldo'] += valor
            self.informacoes_conta['saldo'] -= valor
            hist = (f'Cliente {self.informacoes_cliente["nome"]} '
                    f'transferiu R${valor:.2f} reais para {conta_transferir.informacoes_cliente["nome"]}')
            hist_conta_transferir = (f'Recebeu transferência de {self.informacoes_cliente["nome"]} '
                    f'no valor de R${valor:.2f} reais')
            self.historico_transacoes.insert(0, hist)
            conta_transferir.historico_transacoes.insert(0, hist_conta_transferir)
        else:
            print('Você não pode transferir pois não tem saldo suficiente!')

    def verificarSaldo(self):
        return print(f'Seu saldo é: R${self.informacoes_conta["saldo"]:.2f}')

    def verificarHistorico(self):
        for hist in self.historico_transacoes:
            print(hist)
