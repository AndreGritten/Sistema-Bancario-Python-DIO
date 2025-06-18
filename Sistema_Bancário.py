menu = """
💰 MENU PRINCIPAL 💰

[1] Depositar 🟢
[2] Sacar 🔴
[3] Extrato 📄
[0] Sair ❌
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_DIARIO = 3

while True:

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opcao = input(menu + "Escolha uma opção: ")

    if opcao == "1":
        print("\n📥 DEPÓSITO 📥")
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("✅ Depósito realizado com sucesso!")
        else:
            print("❌ Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        print("\n📤 SAQUE 📤")
        valor = float(input("Informe o valor do saque: R$ "))

        if valor > saldo:
            print("❌ Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("❌ Operação falhou! O valor do saque excede o limite.")

        elif numero_saques > LIMITE_DIARIO:
            print("❌ Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("✅ Saque realizado com sucesso!")

    elif opcao == "3":
        print("\n📄 EXTRATO 📄")
        print("=========================================")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\n💰 Saldo atual: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "0":
        print("\n👋 Saindo... Obrigado por usar nosso sistema!")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        break

    else:
        print("\n⚠️ Operação inválida! Tente novamente.")
