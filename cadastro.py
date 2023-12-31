from pagamento import escolher_plano, escolher_forma_de_pagamento

#LISTAS DOS CADASTRADOS
funcionario_cadastrado = []
cliente_cadastrado = []
nutri_cadastrado = []

funcionario_master = {"nome": "admin", "CPF": "123.321.123-32", "E-mail": "admin@email.com","user": "admin", "senha": "admin"} # usuario admin 
funcionario_cadastrado.append(funcionario_master)

#função - cadastro de clientes
def cad_cliente():
    print('=-='*10)
    print("\nPREENCHA SEUS DADOS A SEGUIR\n")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nasc = input("Data de Nascimento: ")
    end = input("Endereço: ")
    tel = input("Telefone: ")
    email = input("E-mail: ")
    matricula = tel[-4] + dt_nasc[-4]
    cliente = {"nome": nome, "CPF": cpf, "Dt_Nasc": dt_nasc, "Endereço": end, "Telefone": tel, "E-mail": email, "Matrícula":matricula}
    while True: # antes de finalizar a matricula o cliente escolhe um plano e faz o pagamento 
        plano = escolher_plano()
        if plano:
            sucesso_pagamento = escolher_forma_de_pagamento(plano)
            if sucesso_pagamento == True:
                cliente_cadastrado.append(cliente)
                print('=-='*10)
                print('\nMatrícula realizado com sucesso.\n')
                print('=-='*10)
                break
            elif sucesso_pagamento == False:
                continue

#função - cadastro de nutricionista
def cad_nutri():
    print('=-='*10)
    print("\nPREENCHA SEUS DADOS A SEGUIR\n")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nasc = input("Data de Nascimento: ")
    end = input("Endereço: ")
    tel = input("Telefone: ")
    email = input("E-mail: ")
    crn = input("CRN: ")
    nutri = {"nome": nome, "CPF": cpf, "Dt_Nasc": dt_nasc, "Endereço": end, "Telefone": tel, "E-mail": email, "CRN": crn}
    nutri_cadastrado.append(nutri)
    print('=-='*10)
    print("\nParabéns!\nCadastrado com sucesso.\n")
    print('=-='*10)
    
#função - cadastro de funcionario
def cad_funcionario():
    print('=-='*10)
    print("\nPREENCHA SEUS DADOS A SEGUIR\n")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    cont = 0
    while cont == 0:
        user = input('Crie um Login: ')
        for  dicionario in funcionario_cadastrado:
            if user == dicionario["user"]: # verifica se o nome de usuario ja esta sendo utilizado
                print("Este nome ja esta sendo utilizado")
            else:
                cont = 1
    senha = input('Crie uma Senha: ')
    funcionario = {"nome": nome, "CPF": cpf, "E-mail": email,"user": user, "senha":senha}
    funcionario_cadastrado.append(funcionario)
    print('=-='*10)
    print("\nParabéns!\nCadastrado com sucesso.\n")
    print('=-='*10)
