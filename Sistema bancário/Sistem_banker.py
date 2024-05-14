menu = '''

###########################
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair 
###########################

=> '''

valor = 0
deposito_cont = 0
limite_saque = 3
saque = 0
while True:

    escolha = int(input(menu))

    if escolha == 0:
        deposito = int(input("Qual valor deseja depósitar?:  "))
        
        if deposito <= 0:
           print("Deposito inválido, não é permitidos valores menores que 0")
        
        else:
             deposito_cont += 1
             valor += deposito
             print()
             print(f'Valor do depósito de {valor} \n{deposito_cont} depositos feitos hoje. ')
    
    elif escolha == 1:
        print(f"Saldo atual {valor}\nQuantidades de saques livres hoje {limite_saque}")
        valor_saque = int(input('Quanto gostaria de sacar?: '))

        if valor_saque > 500:
            print('Limite por saque excedido, saques até R$500 ')
        
        elif valor_saque > valor:
            print("Sem saldo para sacar")
        
        elif valor_saque < 0:
            print('Valor infálido')

        elif limite_saque < 1:
            print('Saques por dia excedidos, por favor tente amanhã. ')    
       
        else:
            print('Dinheiro retirado com sucesso! ')
            saque += valor_saque
            limite_saque -= 1    
    
    elif escolha == 2:
       print('============EXTRATO===========')
       print(f'Deposito: R$ {valor:.2f}')
       print(f"Saque: R${saque}")
       print(f'Quantidade de depositos feitos hoje: {deposito_cont}')
       print(f'saques restantes  {limite_saque}')


       print(f'Deposito total: R${valor - saque}')
       print('===============================')
    elif escolha == 3:
        break

    else:
        print('Por favor escolha uma das opções')            