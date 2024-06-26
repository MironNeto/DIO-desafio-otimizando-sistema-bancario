menu = """
Escolha a sua operacao desejada:

[d] = depositar
[s] = sacar
[e] = extrato
[u] = criar novo usuario
[c] = criar nova conta corrente
[q] = sair
"""

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3
VALOR_LIMITE_SAQUE = 500
lista_usuarios = {}
lista_contas = []
proxima_conta = 1

def criar_usuario(lista_usuarios):

    cpf = input("Digite o CPF do usuario a ser cadastrado.\n")
    if (cpf in lista_usuarios.keys()):
        print("Usuario ja possui cadastro.")
        return lista_usuarios
    else:
        lista_usuarios_atualizada = lista_usuarios

        nome = input("Digite o nome do usuario\n")

        data_nascimento = input("Digite a data de nascimento do usuario no formato DD/MM/AAAA (apenas os numero).\n")


        logradouro = input("Digite o logradouro do usuario.\n")
        numero = input("Digite o numero do usuario.\n")
        bairro = input("Digite o bairro do usuario.\n")
        cidade = input("Digite o cidade do usuario.\n")
        estado = input("Digite o sigla do estado do usuario.\n")

        endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

        novo_usuario = {cpf: {"nome": nome, "data de nascimento": data_nascimento,"endereco": endereco},}

        lista_usuarios_atualizada.update(novo_usuario)

        return lista_usuarios_atualizada

def criar_conta(lista_contas, lista_usuarios, proxima_conta):
    cpf = input("Digite o CPF do usuario.\n")
    if (cpf in lista_usuarios.keys()):
        numero_conta = proxima_conta
        proxima_conta += 1
        agencia = 1

        lista_contas_atualizada = lista_contas.copy()
        lista_contas_atualizada.append([agencia, numero_conta, cpf])

        return(lista_contas_atualizada, proxima_conta)

    else:
        print("CPF de usuario nao encontrado.")
        return(lista_contas, proxima_conta)

def deposito(saldo, valor, extrato,/):
    
    if(valor <= 0):
        print("Valor do deposito deve ser positivo.")

    else:
        saldo += valor
        extrato += f'Deposito  -------------    R$ {valor:.2f}\n'
        print(f"Depositado valor de R$ {valor:.2f} na conta.")

    return saldo, extrato

def saque(*, saldo, valor, extrato, VALOR_LIMITE_SAQUE, numero_saques, LIMITE_SAQUES_DIARIOS):
    
    if valor <= 0:
        print("Valor do saque deve ser positivo.")

    elif valor > VALOR_LIMITE_SAQUE:
        print("Valor solicitado esta acima do valor limite por saque.")

    elif valor > saldo:
        print("Saldo insuficiente.")

    elif numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("Limite de saques diarios atingido")

    else:
        saldo -= valor
        numero_saques += 1
            
        extrato += f'Saque     -------------    R$ {valor:.2f}\n'
        print(f'Saque realizado no valor de R$ {valor:.2f}')

    return saldo, extrato, numero_saques

def mostrar_extrato(saldo,/,*,extrato):
    print("______________EXTRATO______________")
    print("___________________________________")
        
    print("Nao foram realizadas movimentacoes" if not extrato else extrato)

    print(f'Saldo     -------------    R$ {saldo:.2f}')

    print("___________________________________")


while True:
    
    opcao = input(menu)

    if opcao == "d":
        mensagem = """
Opcao deposito selecionada.
Digite o valor que voce deseja depositar.
"""
        valor = float(input(mensagem))

        saldo, extrato = deposito(saldo, valor, extrato)
        
        
    elif opcao == "s":        
        mensagem = """
Opcao  saque selecionada.
Digite o valor que voce deseja sacar.
"""
        valor = float(input(mensagem))

        saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, numero_saques=numero_saques, VALOR_LIMITE_SAQUE=VALOR_LIMITE_SAQUE, LIMITE_SAQUES_DIARIOS=LIMITE_SAQUES_DIARIOS)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)
        

    elif opcao == "q":
        print("Opcao sair selecionada.")
        break
    
    elif opcao == "u":
        lista_usuarios = criar_usuario(lista_usuarios)
        print(lista_usuarios)

    elif opcao == "c":
        lista_contas, proxima_conta = criar_conta(lista_contas, lista_usuarios, proxima_conta)
        print(lista_contas)

    else:
        print("Opcao selecionada e invalida. Por favor, selecione novamente a operacao desejada.")