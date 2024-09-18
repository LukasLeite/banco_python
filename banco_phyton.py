menu = """
Qual operação deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)
   
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")
            print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("ERRO! Você não tem saldo suficiente.")
            print(f"\nSaldo: R$ {saldo:.2f}")

        elif excedeu_limite:
            print("ERRO! O valor do saque excede o limite. Digite um valor até 500$")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            print(f"Saques realizados: {numero_saques: .0f}")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n|================ EXTRATO ================|")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("|==========================================|")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")