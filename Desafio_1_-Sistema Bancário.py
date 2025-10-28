menu = """

[1] Deposito
[2] Saque
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("FALHA! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        ultrapassou_saldo = valor > saldo

        ultrapassou_limite = valor > limite

        ultrapassou_saques = numero_saques >= LIMITE_SAQUES

        if ultrapassou_saldo:
            print("FALHA! Você não tem saldo suficiente.")

        elif ultrapassou_limite:
            print("FALHA! O valor do saque ultrapassa o limite.")

        elif ultrapassou_saques:
            print("FALHA! Número máximo de saques ultrapassado.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("FALHA! O valor informado é inválido.")

    elif opcao == "3":
        print("\n---------------- EXTRATO ----------------")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-----------------------------------------")

    elif opcao == "0":
        break

    else:

        print("INVÁLIDO, por favor selecione novamente a operação desejada.")



