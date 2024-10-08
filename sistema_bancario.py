menu = """
*****
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

*****
Digite sua opção:
"""
saldo = 0
limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")        
        
        deposito = float(input("Digite o valor para depositar: "))
        if deposito <= 0:
            print("Valor para depósito inválido...")
        
        else:
            saldo += deposito
            extrato += f"Depósito: + R$ {deposito:.2f}\n"        
    
    elif opcao == "s":
        print("Saque")
                   
        if numero_saques >= LIMITE_SAQUE:
            print("Você ultrapassou o número de vezes para Saque...")
        
        else:
            saque = float(input("Digite o valor para sacar: "))
            if saque > 500:
                print("O valor máximo permitido para saque é de 500...")

            elif saque > saldo:
                print("Seu saldo é insuficiente para realização deste saque...")
                
            else:
                saldo -= saque
                extrato += f"Saque: - R$ {saque:.2f}\n"
                numero_saques += 1                

    elif opcao == "e":
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break
    else:
        print("Opção Inválida!!")
