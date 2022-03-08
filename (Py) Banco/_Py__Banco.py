import Conta

saldo_inicial = 0.0
conta1 = Conta.Conta(saldo_inicial = 0.0)

print('O saldo inicial e {}\n'.format(conta1.set_saldo))

while True:
    print('D - Depositar valor')
    print('S - Sacar valor')
    print('E - Obtem saldo')
    print('X - Sair')

    opcao = input('\nSelecione uma opcao: ').upper()



    if opcao == 'D':
        try:
            valor_deposito = float(input('Qual o valor que deseja depositar?\n'))
        except:
            print('Erro! Apenas valores numericos para deposito!\n')
        else:
            conta1.deposito(valor_deposito)
            print("Seu novo saldo e R$ {}\n\n".format(conta1.set_saldo))

    elif opcao == 'S':
        try:
            valor_saque = float(input('Qual o valor que deseja sacar?\n'))
        except:
            print('Erro! Apenas valores numericos para saque!\n')
        else:
            conta1.saque(valor_saque)
            print ('Seu saldo atual e R$ {}\n'.format(conta1.set_saldo))
        
    elif opcao == 'E':
        print ('Seu saldo atual e R$ {}\n'.format(conta1.set_saldo))

    elif opcao == 'X':
        print ('\nAte a proxima!\n\n')
        break