def sacar(*, saldo, extrato, saques_diarios, saques, limite_saque):
    valor = float(input("Digite o valor do saque: "))
    if valor > limite_saque:
        print("\nValor excede limite de saque.\nPor favor, insira um valor de até " + str(limite_saque))
    elif valor > saldo:
        print("\nSaldo insuficiente!\nValor solicitado excede saldo disponível")
    elif saques >= saques_diarios:
        print("\nLimite de saques diarios atingido!")
    elif valor > 0:
        saldo -= valor
        atualizar = f"\nSaque de R$ {valor:.2f} realizado com sucesso!"
        extrato = extrato + atualizar
        saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nValor inválido!\n")
    
    return saldo, extrato, saques

def depositar(saldo, extrato, /):
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        atualizar = f"\nDepósito de R$ {valor:.2f} realizado com sucesso!"
        extrato = extrato + atualizar
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    else:
            print("\nValor de depósito inválido!")
    
    return saldo, extrato

def ver_extrato(saldo, /, *, extrato):        
    print(f''' -----------------------------
        {extrato}\n -----------------------------
        Saldo atual: {saldo:.2f}
        ''')    

def mostrar_operacoes():
    opcao = '''
================================
      Selecione uma opção:
          
    [1] Saque
    [2] Depósito
    [3] Extrato
    [0] Encerrar
================================\n\t
'''
    return input(opcao) 

def avaliar_cliente(cpf, usuarios):
    busca_usuario = [ usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return busca_usuario[0] if busca_usuario else 0

def cadastrar_cliente(usuarios):
    cpf = input("Insira seu CPF: ")
    usuario = avaliar_cliente(cpf, usuarios)
    if usuario:
        print("Usuario já possui cadastro!\nAcesse sua conta ou prossiga para a crição de uma")
        return
    nome = input("Insira nome completo: ")
    data_nascimento = input("Insira sua data de nascimento(DD/MM/AAAA): ")
    endereco = input("Informe seu endereco(logradouro, n° - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf" : cpf, "endereco": endereco})

def criar_conta(agencia, usuarios, numero_conta):
    cpf = input("Insira seu CPF: ")
    usuario = avaliar_cliente(cpf, usuarios)
    if usuario != 0:
        print("Conta criada com sucesso!")
        conta = ({"agencia": agencia, "numero_conta": numero_conta, "usuario" : usuario})
        extrato = ({"nome" : usuario["nome"], "cpf" : cpf, "numero_conta": numero_conta, "extrato": "", "saldo" : 0})
        return conta, extrato
    else:
        print("Usuario não encontrado")
        return None, None
    
def iniciar_banco():
    tela = '''
====================================
    Bem vindo(a) ao nosso banco!
-------------------------------------
    Selecione uma opção:
-------------------------------------\n
    [1] Já sou cliente e possuo conta
    [2] Ainda não sou cliente ou quero criar uma conta\n
====================================
    '''
    return input(tela)

def identificar_cadastro():
    tipo =  '''
    [1] Não possuo cadastro no banco
    [2] Já possuo cadastro e quero abrir uma nova conta\n
    '''
    return input(tipo)

def buscar_extrato(numero_conta, extrato_contas):

    busca_extrato = [conta for conta in extrato_contas if conta["numero_conta"] == numero_conta]

    if busca_extrato:

        return busca_extrato[0]["extrato"], busca_extrato[0]["saldo"], busca_extrato[0]["nome"] if busca_extrato else None
    else:
        print("Conta não encontrada")
        return None, None, None

def usar_conta(usuarios, contas, extrato_contas):
    SAQUES_DIARIOS = 3
    LIMITE_SAQUE = 500    
    saques = 0

    numero_conta = int(input("\nDigite o número da conta: "))
    extrato, saldo, nome = buscar_extrato(numero_conta, extrato_contas)
    if nome:
        print(f'Olá {nome}\n')
        while True:
            opcao = mostrar_operacoes()

            if opcao == '1':
                saldo, extrato, saques = sacar(saldo=saldo, extrato = extrato, saques_diarios = SAQUES_DIARIOS, saques = saques, limite_saque = LIMITE_SAQUE)
        
            elif opcao == '2':
                saldo, extrato = depositar(saldo, extrato)
        
            elif opcao == '3':
                ver_extrato(saldo, extrato=extrato)
            elif opcao == '0':
                for conta in extrato_contas:
                    if numero_conta == conta["numero_conta"]:
                        conta["extrato"] = extrato
                        conta["saldo"] = saldo
                print("Obrigado por utilizar nossos serviços!\nVolte sempre!")
                break
            else:
                print("Opção inválida") 
    else:
        print("Insira uma conta existente")
        return

def selecionar_uso():
    message = '''
    [1] Saldo, saque, extrato
    [2] Ver número da conta(Primeiro acesso)
    '''
    return input(message)

def encontrar_conta(contas):

    cpf = input("Insira seu cpf: ")

    numero_conta = [conta["numero_conta"] for conta in contas if conta["usuario"]["cpf"] == cpf]

    if numero_conta:
        numero_conta = numero_conta[0]
        print("O número de sua conta é: " + str(numero_conta))

    else:
        print("Conta não encontrada")

def main():
    AGENCIA = "0001" #Global = usar em criar conta e acessar conta
    usuarios = []
    contas = []
    extrato_contas = []

    while True:
        opcao = iniciar_banco()
        if opcao == '1':
            uso = selecionar_uso()
            if uso == '1':
                usar_conta(usuarios, contas, extrato_contas)
            elif uso == '2':
                encontrar_conta(contas)
            else:
                print("\nOpção inválida")
        elif opcao == '2':
            tipo = identificar_cadastro()
            if tipo == '1':
                cadastrar_cliente(usuarios)
            elif tipo == '2':
                numero_conta = len(contas) + 1
                conta, extrato = criar_conta(AGENCIA, usuarios, numero_conta)
                if conta:
                    contas.append(conta)
                    extrato_contas.append(extrato)
            else:
                print("Opção inválida!")

        print(usuarios)
        print(contas)

        print(extrato_contas)
main()