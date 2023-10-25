#LISTAS DOS CADASTRADOS
cliente_cadastrado = []
nutri_cadastrado = []
personal_cadastrado = []

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
    print('=-='*10)
    print("\nParabéns!\nCadastrado com sucesso.\n")
    print('=-='*10)
    cliente = {"nome": nome, "CPF": cpf, "Dt_Nasc": dt_nasc, "Endereço": end, "Telefone": tel, "E-mail": email, "Matrícula":matricula}
    cliente_cadastrado.append(cliente)

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
    matricula = tel[-4] + dt_nasc[-4]
    print('=-='*10)
    print("\nParabéns!\nCadastrado com sucesso.\n")
    print('=-='*10)
    nutri = {"nome": nome, "CPF": cpf, "Dt_Nasc": dt_nasc, "Endereço": end, "Telefone": tel, "E-mail": email, "CRN": crn, "Matrícula":matricula}
    nutri_cadastrado.append(nutri)

#função - cadastro de personal
def cad_personal():
    print('=-='*10)
    print("\nPREENCHA SEUS DADOS A SEGUIR\n")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nasc = input("Data de Nascimento: ")
    end = input("Endereço: ")
    tel = input("Telefone: ")
    email = input("E-mail: ")
    cref = input("CREF: ")
    matricula = tel[-4] + dt_nasc[-4]
    print('=-='*10)
    print("\nParabéns!\nCadastrado com sucesso.\n")
    print('=-='*10)
    personal = {"nome": nome, "CPF": cpf, "Dt_Nasc": dt_nasc, "Endereço": end, "Telefone": tel, "E-mail": email, "CREF": cref, "Matrícula":matricula}
    personal_cadastrado.append(personal)