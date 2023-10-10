import myImports.utils as utils
from myImports.controleBancario import criarBancaria
from random import randint
from os import system

def criar_numero_id():
    while True:
        numero = randint(1000, 9999)
        if numero not in used:
            used.append(numero)
            break
    return numero

if __name__ == '__main__':
    sistema_ativo = 1
    usuarios = []
    used = [5555, 6666]
    cliente_padrao1 = criarBancaria('Breno',  'Rua das Cores', '+5579912345678',
                                    'noreply@hotmail.com', '07/05/1998', 5555, True)
    cliente_padrao1.depositar(5500)
    cliente_padrao2 = criarBancaria('John', 'Rua das Formigas', '+5579987654321',
                                    'replyme@hotmail.com', '24/12/1980', 6666, False)
    cliente_padrao2.depositar(9872)
    usuarios.append(cliente_padrao1)
    usuarios.append(cliente_padrao2)

    logado = False
    while sistema_ativo == 1:
        mn_nav = 0
        utils.criarMenu('Bem-vindo ao Nosso Sistema')
        while not logado:
            ask_usr = input('LOGIN\n'
                            '[0] admin\n'
                            '[1] cliente\n'
                            '[2] Sair\n'
                            '>>> ')
            if ask_usr == '2':
                sistema_ativo = 0
                break
            if ask_usr == '0':
                senha = input('Senha: ')
            elif ask_usr == '1':
                usuario = input('Usuário: ')
                senha_cliente = utils.validarInt(input('Número: '))
            else:
                system('cls')
                continue
            logado = True
        system('cls')
        while logado:
            if ask_usr == '0' and senha == 'admin':
                menu_nav = input('[1] Cadastrar Clientes\n'
                                 '[2] Editar Conta\n'
                                 '[3] Apagar Conta\n'
                                 '[4] Listar Usuários\n'
                                 '[0] Sair\n'
                                 '>>> ')
                system('cls')
                if menu_nav == '1':
                    print('Por favor, insira as informações que se pedem:')
                    numero = criar_numero_id()
                    nome = input('Digite seu nome completo: ')
                    endereco = input('Digite seu endereço: ')
                    telefone = input('Nº de telefone: ')
                    email = input('Seu melhor e-mail: ')
                    dt_nasc = input('Sua data de nascimento (dd/mm/yy): ')
                    while '/' not in dt_nasc or len(dt_nasc) < 8:
                        print('Digite uma data válida!')
                        dt_nasc = input('Sua data de nascimento (dd/mm/yy): ')
                    system('cls')
                    tipo_conta = utils.validarInt(input('Escolha o tipo da conta:\n'
                                       '[1] Corrente\n'
                                       '[2] Poupança\n'
                                       '>>> '))
                    system('cls')
                    if tipo_conta == '1':
                        tipo_conta = True
                    else:
                        tipo_conta = False
                    cliente = criarBancaria(nome, endereco, telefone, email, dt_nasc, numero, tipo_conta)
                    usuarios.append(cliente)

                if menu_nav == '2':
                    escolher_user = input('Digite o nome do usuário: ')
                    for usr in usuarios:
                        if len(usuarios) == 0:
                            pass
                        else:
                            if escolher_user == usr.informacoes_cliente['nome']:
                                usr.editarConta()

                if menu_nav == '3':
                    escolher_user = input('Digite o nome do usuário: ')
                    for usr in usuarios:
                        if len(usuarios) == 0:
                            pass
                        else:
                            if escolher_user == usr.informacoes_cliente['nome']:
                                usr.excluirConta()

                if menu_nav == '4':
                    utils.criarMenu('Lista de Clientes')
                    keywords = ['Nome', 'Endereço', 'Telefone', 'E-mail', 'Nascimento', 'Conta Corrente',
                                'Conta Poupança', 'Senha', 'Saldo']
                    for usr in usuarios:
                        for k,v in enumerate(usr.informacoes_cliente.values()):
                            print(f'{keywords[k]}: {v}')
                        for k,v in enumerate(usr.informacoes_conta.values()):
                            if keywords[k + 5] == 'Saldo':
                                print(f'{keywords[k]}: R${v:.0f},00')
                            else:
                                print(f'{keywords[k + 5]}: {v}')
                        print('-'*30)
                    input('Aperte ENTER para sair')

                if menu_nav == '0':
                    logado = False
                    break
                system('cls')

            if ask_usr == '1':
                for usr in usuarios:
                    if (usuario == usr.informacoes_cliente.get('nome') and
                            senha_cliente == usr.informacoes_conta.get('numero')):
                        usuario = usr
                        while True:
                            system('cls')
                            menu_nav = input('[1] Depositar\n'
                                             '[2] Sacar\n'
                                             '[3] Transferir\n'
                                             '[4] Verificar Saldo\n'
                                             '[5] Ver histórico de transações\n'
                                             '[0] Sair\n'
                                             '>>> ')
                            system('cls')
                            if menu_nav == '1':
                                valor = utils.validarInt(input('Digite o valor a depositar: '))
                                usuario.depositar(valor)

                            if menu_nav == '2':
                                valor = utils.validarInt(input('Digite o valor a sacar: '))
                                usuario.sacar(valor)

                            if menu_nav == '3':
                                while True:
                                    destino = input('Para quem quer transferir (insira o nome do usuário): ')
                                    while destino == usuario.informacoes_cliente.get('nome'):
                                        print('Você não pode transferir para si mesmo!')
                                        destino = input('Para quem quer transferir (insira o nome do usuário): ')
                                    for usr in usuarios:
                                        if destino == usr.informacoes_cliente['nome']:
                                            destino = usr
                                    if isinstance(destino, str):
                                        print('Este usuário não existe!')
                                        continue
                                    break
                                quantia = utils.validarFloat(input('Valor a transferir:  R$'))
                                usuario.transferir(destino, quantia)

                            if menu_nav == '4':
                                usuario.verificarSaldo()
                                input('Aperte ENTER para sair')

                            if menu_nav == '5':
                                usuario.verificarHistorico()
                                print('-'*30, '\nAperte ENTER para sair')
                                input()

                            if menu_nav == '0':
                                logado = False
                                mn_nav = 1
                                break

                    if senha_cliente != usr.informacoes_conta.get('numero') and mn_nav == 0:
                        system('cls')
                        print('Senha incorreta!')
                        logado = False

    utils.criarMenu('Volte Sempre!')
