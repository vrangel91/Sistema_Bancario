# Menu do Usuário
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

# Variáveis
saldo = 0
extrato = ''
numero_saque = 3
limite_saque = 500
LIMITES_SAQUES = 0

# Loop
while True:
    opcao = input(menu).lower()

    #  Escolhendo a opção depositar
    if opcao == '1':
        deposito = float(input('Digite o valor: '))
        if deposito <= 0:
            print('Erro - Deposito deve ser maior que R$ 0,00 Reais')
        else:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
            print('Saldo: R$ {:.2f}'.format(saldo))

    #  Escolhendo a opção sacar
    elif opcao == '2':
        sacar = float(input('Digite o valor: '))

        if sacar > saldo:
            print('Saque não autorizado!')

        elif sacar <= 0:
            print('Erro - Saque deve ser maior que R$ 0,00 Reais.')

        elif LIMITES_SAQUES == 3 or sacar > limite_saque:
            print('Saque não autorizado, limite 3 Saques atingido.')

        else:
            saldo -= sacar
            extrato += f'Saque: R$ {sacar:.2f}\n'
            LIMITES_SAQUES += 1
            print('Saldo: R$ {:.2f}'.format(saldo))

    # Mostrando extrato da conta
    elif opcao == '3':
        print("\n============ EXTRATO ============")
        print('Não foram existe movimentações realizadas. 'if not extrato else extrato)
        print('\nSaldo: R$ {:.2f}'.format(saldo))
        print("=================================")

    # Saindo do programa
    elif opcao == '4':
        print('Saindo do programa, Volte sempre!')
        break
    # Mensagem caso digite uma opção inválida
    else:
        print('Digite uma opção válida')



