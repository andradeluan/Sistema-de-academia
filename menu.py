import cadastro
import nutricionista

opcao = 0

while opcao != 3:
    # Menu Principal:
    print('=-='*10)
    print("\nACADEMIA FIT GYM\nPara você deixar sua saúde em dia!\n")
    print("\n [ 1 ] Entrar\n [ 2 ] Cadastro\n [ 3 ] Sair\n")
    print('=-='*10)
    opcao = int(input('\nEscolha uma opção: '))
    print('=-='*10)
    # Opção ENTRAR
    if opcao == 1:
        verificador_user = input('Digite seu Login: ')
        verificador_senha = input('Digite sua Senha: ')
        for  dicionario in cadastro.funcionario_cadastrado:
            if verificador_user == dicionario["user"]: # verifica se o usuario existe
                if verificador_senha == dicionario["senha"]: # verifica se a senha do usuario estar correta
                    # Menu do funcionário logado
                    while True: 
                        print('=-='*10)
                        print("\n[ 1 ] Cadastros\n[ 2 ] Nutricionista\n[ 3 ] Voltar\n")
                        print('=-='*10)
                        op = int(input('\nEscolha uma opção: '))
                        if op == 1: # Menu para cadastro 
                            while True:
                                print("\nCADASTRAR COMO\n")
                                print("\n [ 1 ] Cliente\n [ 2 ] Nutricionista\n [ 3 ] Voltar\n")
                                cad = int(input("\nEscolha uma opção: "))
                                print('=-='*10)
                                if cad == 1: # chama a função de cadastro de clientes
                                    cadastro.cad_cliente()
                                    break
                                elif cad == 2: # chama função de cadastro de nutricionista
                                    cadastro.cad_nutri()
                                    break
                                elif cad == 3: # Volta pro Menu Principal
                                    print('=-='*10)
                                    print("Carregando...")
                                    print('=-='*10)
                                    break
                                else: # mensagem quando é selecionado uma Opção Inválida
                                    print('=-='*10)
                                    print("\nOpção inválida\n")
                                    print('=-='*10)
                        elif op == 2:# chama a funçao com serviços de nutricionistas 
                            nutricionista.nutri()
                        elif op == 3: # volta para o menu principal
                            break
                        else: # mensagem quando é selecionado uma Opção Inválida
                            print('=-='*10)
                            print("\nOpção inválida\n")
                            print('=-='*10)
                else: # mensagem de Login ou senha invalida
                    print('=-='*10)
                    print("\nLogin ou Senha inválida\n")
                    print('=-='*10)
                    ent=0
    elif opcao == 2: # Opção CADASTRO (de funcionário)
        cadastro.cad_funcionario()
    elif opcao == 3: # Opção SAIR/Fechar o programa
        print()
        print('=-='*10)
        print("Finalizando...")
        print('=-='*10)
        break
    # mensagem quando é selecionado uma Opção Inválida
    else:
        print("Opção Inválida!\n Tente novamente.\n")
print("\nVOLTE SEMPRE!\n")