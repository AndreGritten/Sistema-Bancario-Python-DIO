import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso!")
    else:
        print("❌ Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("❌ Operação falhou! Você não tem saldo suficiente.")

    elif valor > limite:
        print("❌ Operação falhou! O valor do saque excede o limite.")

    elif numero_saques >= limite_saques:
        print("❌ Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso!")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo,/,*,extrato):
    print("\n📄 EXTRATO 📄")
    print("=========================================")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):
    while True:    
        cpf = input("Informe o CPF do usuário (somente números): ")
        if len(cpf) == 11 and cpf.isdigit():
            break
        else:
            print("CPF deve conter 11 números!!!")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!!!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)

    print(f"Usuário {nome} cadastrado com sucesso!!!")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário para criar uma conta(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        nova_conta = {
            "agencia": agencia, 
            "numero_conta": numero_conta, 
            "usuario": usuario
            }
        contas.append(nova_conta)
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        print(f"""Agência:\t{conta["agencia"]}
C/C:\t{conta["numero_conta"]}
Titular:\t{conta["usuario"]["nome"]}
""")


def main():
    LIMITE_DIARIO = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if opcao == "d":
            print("\n📥 DEPÓSITO 📥")
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            print("\n📤 SAQUE 📤")
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_DIARIO
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            criar_conta(AGENCIA, contas, usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\n👋 Saindo... Obrigado por usar nosso sistema!")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            break

        else:
            print("\n⚠️ Operação inválida! Tente novamente.")

if __name__ == "__main__":
    main()
