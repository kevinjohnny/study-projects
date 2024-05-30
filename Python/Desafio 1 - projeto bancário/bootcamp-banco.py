#Deposito, saque, saldo e extrato
#Depositar valores POSITIVOS
#Depositos armazenados em uma variavel e aparecer em extrato
#Permitir apenas 3 saques diarios, com maximo de 500 reais por saque
#Se o saldo for inferior ao valor do saque, informar que não será possível sacar devido a falta de saldo
#Saldos devem ser armazenados numa variável e exibidos em extrato
#O extrato deve exibir todas as operações e seus tipos em ordem e no final o saldo atual da conta
menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
'''

LIMITE_SAQUE = 500
SAQUES_DIARIOS = 3
saldo = 0
saques = 0
extrato = ""
loop = 0
while True:
    opcao = input(menu)
    if opcao == "1":
        deposito = float(input("Digite o valor do depósito: "))
        if deposito <= 0:
            print("Valor inválido. Por favor, deposite um valor maior que 0")
        else:
            loop += 1
            saldo = saldo + deposito
            extrato = extrato + "\n[" +str(loop) + "] Depósito: R$ " + str(deposito)
            print("\nDepósito de R$" + str(deposito) + " realizado com sucesso!")
    elif opcao == "2":
        saque = float(input("Digite o valor do saque: "))
        if saque > LIMITE_SAQUE:
            print("\nValor excede limite de saque. Por favor, insira um valor de até " + str(LIMITE_SAQUE))
        elif saque >= saldo:
            print("\nSaldo insuficiente")
        elif saques >= SAQUES_DIARIOS:
            print("\nLimite de saques diarios atingido")
        else:
            loop += 1
            saldo = saldo - saque
            extrato = extrato + "\n[" + str(loop) + "]Saque: R$ " + str(saque)
            saques += 1
            print("\nSaque de " + str(saque) + " realizado com sucesso!")
    elif opcao == "3":
        print(f'''{extrato}\n -----------------------------
        Saldo atual: {saldo:.2f}
        ''')
      #  print(extrato +"\nSaldo atual: " +str(saldo))
    elif opcao == "0":
        break
    else:
        print("\nOpção inválida")   
print(loop)
