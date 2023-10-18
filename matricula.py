#Lista vazia para armazenar os usuários matriculados
aluno_matriculado = []
nutri_matriculado = []
personal_matriculado = []

#Usuário escolhe a opção de matrícula
print("SESSÃO MATRÍCULA\n 1- Aluno\n 2- Nutricionista\n 3- Personal")
usuario = input("\nMatricular como: ")

if usuario == "1": #Aluno
    nome = input("Seu nome completo: ")
    cpf = input("CPF: ")
    data_nasc = input("Data de Nacimento: ")
    endereco = input("Endereço: ")
    tel = input("Número de Telefone: ")
    email = input("E-mail: ")
    numero_matricula = tel[-4:] + data_nasc[-4:]
    
    #Adicionando os dados na lista de alunos matriculados
    aluno = {"Nome": nome, "CPF": cpf, "Data Nas.": data_nasc, "Endereco": endereco, "Telefone": tel, "E-mail": email,"Matrícula": numero_matricula}
    aluno_matriculado.append(aluno)
    print("\nAluno matriculado com sucesso!")

elif usuario == "2": #Nutricionista
    nome = input("Nome Completo: ")
    cpf = input("CPF: ")
    data_nasc = input("Data de Nacimento: ")
    endereco = input("Endereço: ")
    tel = input("Número de Telefone: ")
    email = input("E-mail: ")
    crn = input("CRN: ")
    numero_matricula = tel[-4:] + data_nasc[-4:]

    #Adicionando os dados na lista de nutricionistas matriculados
    nutri = {"Nome": nome, "CPF": cpf, "Data Nas.": data_nasc, "endereco": endereco, "Telefone": tel, "E-mail": email,"CRN": crn, "Matrícula": numero_matricula}
    nutri_matriculado.append(nutri)
    print("\nMatriculado com sucesso!")

elif usuario == "3": #Personal
    nome = input("Nome Completo: ")
    cpf = input("CPF: ")
    data_nasc = input("Data de Nacimento: ")
    endereco = input("Endereço: ")
    tel = input("Número de Telefone: ")
    email = input("E-mail: ")
    cref = input("CREF: ")
    numero_matricula = tel[-4:] + data_nasc[-4:]

    #Adicionando as informações na lista de personal matriculados
    personal = {"Nome": nome, "CPF": cpf, "Data Nas.": data_nasc, "endereco": endereco, "Telefone": tel, "E-mail": email,"CREF": cref, "Matrícula": numero_matricula}
    personal_matriculado.append(personal)
    print("\nMatriculado com sucesso!")
else:
    print("\nInformação inválida.")