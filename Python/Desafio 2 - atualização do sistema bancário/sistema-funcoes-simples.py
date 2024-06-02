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
        extrato = extrato + "\nSaque: R$ " + str(valor)
        print(extrato)
        saques += 1
        print("\nSaque de " + str(valor) + " realizado com sucesso!")
    else:
        print("\nValor inválido!\n")
    
    return saldo, extrato, saques

def depositar(saldo, extrato, /):
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato = extrato + "\nDepósito: R$ " + str(valor)
        print("\nDepósito de R$" + str(valor) + " realizado com sucesso!")
    else:
            print("\nValor de depósito inválido!")
    
    return saldo, extrato

def ver_extrato(saldo, /, *, extrato):        
    print(f''' -----------------------------
        {extrato}\n -----------------------------
        Saldo atual: {saldo:.2f}
        ''')    

def mostrar_menu():
    opcao = input('''
================================
      Selecione uma opção:
          
    [1] Saque
    [2] Depósito
    [3] Extrato
    [4] Cadastrar novo usuario
    [5] Criar nova conta
    [0] Encerrar
================================\n\t
''')
    return opcao   

def avaliar_cliente(cpf, usuarios):
    busca_usuario = [ usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return busca_usuario[0] if busca_usuario else None

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
    if usuario:
        print("Conta criada com sucesso!")
        return ({"agencia": agencia, "numero_conta": numero_conta, "usuario" : usuario})
    print("Usuario não encontrado")

def main():
    AGENCIA = "0001"
    saldo = 0
    saques = 0
    extrato = ""
    SAQUES_DIARIOS = 3
    LIMITE_SAQUE = 500    
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = mostrar_menu()

        if opcao == '1':
            saldo, extrato, saques = sacar(saldo=saldo, extrato = extrato, saques_diarios = SAQUES_DIARIOS, saques = saques, limite_saque = LIMITE_SAQUE)
        
        elif opcao == '2':
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == '3':
            ver_extrato(saldo, extrato=extrato)
        
        elif opcao == '4':
            cadastrar_cliente(usuarios)
        
        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, usuarios, numero_conta)
            contas.append(conta)
        
        elif opcao == '0':
            print("Obrigado por utilizar nossos serviços!\nVolte sempre!")
            break
        else:
            print("Opção inválida") 

main()
