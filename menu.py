import cadastro
import nutricionista

opcao = 0

while opcao != 3:
    
    #Menu Principal:
    print('=-='*10)
    print("\nACADEMIA FIT GYM\nPara você deixar sua saúde em dia!\n")
    print("\n [ 1 ] Entrar\n [ 2 ] Cadastro\n [ 3 ] Sair\n")
    print('=-='*10)
    opcao = int(input('\nEscolha uma opção: '))
    print('=-='*10)

    #Opção ENTRAR
    if opcao == 1:
        for dicionario in cadastro.funcionario_cadastrado:
            verificador_user = input('Digite seu Login: ')
            verificador_senha = input('Digite sua Senha: ')
            #Menu do funcionário logado
            if verificador_user == dicionario["user"] and verificador_senha == dicionario["senha"]:
                ent=0
                while ent != 1:        
                    print('=-='*10)
                    print("\n[ 1 ] Cadastros\n[ 2 ] Nutricionista\n[ 3 ] Personal\n[ 4 ] Voltar\n")
                    print('=-='*10)
                    opcao = int(input('\nEscolha uma opção: '))
                    if opcao == 1:
                        print("\nCADASTRAR COMO\n")
                        print("\n [ 1 ] Cliente\n [ 2 ] Nutricionista\n [ 3 ] Personal\n [ 4 ] Voltar\n")
                        cad = int(input("\nEscolha uma opção: "))
                        print('=-='*10)
                        while cad != 4:
                            #chama a função de cadastro de clientes
                            if cad == 1:
                                #import cadastro
                                cadastro.cad_cliente()
                                cad = 4
                            #chama função de cadastro de nutricionista
                            elif cad == 2:
                                #import cadastro
                                cadastro.cad_nutri()
                                cad = 4
                            #chama função de cadastro de personal
                            elif cad == 3:
                                #import cadastro
                                cadastro.cad_personal()
                                cad = 4
                            #Volta pro Menu Principal
                            elif cad == 4:
                                print('=-='*10)
                                print("Carregando...")
                                print('=-='*10)
                            #nem um nem outro
                            else:
                                    print('=-='*10)
                                    print("\nOpção inválida\n")
                                    print('=-='*10)
                                    cad = 4
    
                    elif opcao == 2:
                      nutricionista.nutri()  
                    #elif opcao == 3:
                    elif opcao == 4:
                        ent = 1
                    else:
                       print('=-='*10)
                       print("\nOpção inválida\n")
                       print('=-='*10)
            else:
                print('=-='*10)
                print('Login ou Senha estão incorretos.\nTente novamente')
                print('=-='*10)

    #Opção CADASTRO (de funcionário)
    elif opcao == 2:
        cadastro.cad_funcionario()

    #Opção SAIR
    elif opcao == 3:
        print()
        print('=-='*10)
        print("Finalizando...")
        print('=-='*10)
    
    #nem um nem outro
    else:
        print("Opção Inválida!\n Tente novamente.\n")
print("\nVOLTE SEMPRE!\n")