import os

saldo = 0
extrato_deposito = ""
transacao_deposito = 0
extrato_saque = ""
transacao_saque = 0
limite_saque = 1
valor_limite = 500

while True:
    menu = input("Menu Principal\n\n01. Depósito\n02. Saque\n03. Menu Extrato\n\n09. Sair\n\nSua resposta: ")

    if menu.isdigit():
        os.system('cls')
        menu = int(menu)

        if menu == 1:
            valor_deposito = input('Qual o valor que deseja depositar?\n\nValor: ')
            
            if valor_deposito.isdigit():
                valor_deposito = int(valor_deposito)
                transacao_deposito += 1
                saldo = saldo + valor_deposito
                extrato_deposito = extrato_deposito + f'{transacao_deposito} deposito: ' + str(f'R$ {valor_deposito:.2f}') + "\n"

                os.system('cls')
                print(f'Deposito de R$ {valor_deposito:.2f} realizado com sucesso.\n')

            else:
                print(f'Não foi possível despositar, verifique se digitou um número válido. "{valor_deposito}"')

        elif menu == 2:
            valor_saque = input('Qual o valor que deseja sacar?\n\nValor: ')

            if valor_saque.isdigit():
                valor_saque = int(valor_saque)

                if valor_saque <= valor_limite and limite_saque <= 3 and saldo > valor_saque:
                    limite_saque += 1
                    saldo = saldo - valor_saque
                    transacao_saque += 1
                    extrato_saque = extrato_saque + f'{transacao_saque} saque: ' + str(f'R$ {valor_saque:.2f}') + "\n"

                    os.system('cls')
                    print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso.\n')
                
                elif valor_saque > valor_limite:
                    os.system('cls')
                    print(f'Error ao sacar o Valor do saque é "R$ {valor_saque:.2f}" \nLimite de saque é "R$ {valor_limite:.2f}\n"')

                elif saldo < valor_saque:
                    os.system('cls')
                    print(f'Error ao sacar!\n\nO valor de saque "R$ {valor_saque:2f}" é superior do seu saldo "R$ {saldo:.2f}" disponível.\n')

                elif limite_saque >= 3:
                    os.system('cls')
                    print('Numeros de saques permitidos foram atingidos.\n')

            else:
                os.system('cls')
                print('Valor inválido, digite um valor válido.\n')

        elif menu == 3:
            while True:
                menu_extrato = input("Menu Extrato\n\n01. Consultar transações de Depósito\n02. Consultar transações de Saque\n03. Saldo Atual\n\n09. Sair\n\nSua resposta: ")

                if menu_extrato.isdigit():
                    menu_extrato = int(menu_extrato)

                    if menu_extrato == 1:
                        os.system('cls')
                        print(f'Extrato de Depósito:\n{extrato_deposito}')

                    elif menu_extrato == 2:
                        os.system('cls')
                        print(f'Extrato de Saque:\n{extrato_saque}')
                    
                    elif menu_extrato == 3:
                        os.system('cls')
                        print(f'Seu saldo é de R$ {saldo:.2f}\n')

                    elif menu_extrato == 9:
                        os.system('cls')
                        break
                    else:
                        print('Valor inválido. digite um valor válido.\n')
                else:
                    print('Valor inválido. digite um valor válido.\n')

        elif menu == 9:
            print('Obrigado por usar nossos serviços.\n')
            break

        else:
            print(f'Valor {menu} não foi reconhecido no menu, por favor, escolha uma das opções.\n')
    
    else:
        print(f'Valor {menu} não foi reconhecido no menu, por favor, escolha uma das opções.\n')