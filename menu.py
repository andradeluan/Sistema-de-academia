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
        print("login e senha")

    #Opção CADASTRO
    elif opcao == 2:
        print('=-='*10)
        print("\nCADASTRAR COMO\n")
        print("\n [ 1 ] Cliente\n [ 2 ] Nutricionista\n [ 3 ] Personal\n [ 4 ] Menu Principal\n")
        cad = int(input("\nEscolha uma opção: "))
        print('=-='*10)

        while cad != 4:
            #chama a função de cadastro de clientes
            if cad == 1:
                import cadastro
                cadastro.cad_cliente()
                cad = 4

            #chama função de cadastro de nutricionista
            elif cad == 2:
                import cadastro
                cadastro.cad_nutri()
                cad = 4
            
            #chama função de cadastro de personal
            elif cad == 3:
                import cadastro
                cadastro.cad_personal()
                cad = 4
            
            #Volta pro Menu Principal
            elif cad == 4:
                print('=-='*10)
                print("Voltando ao Menu Principal...")
                print('=-='*10)
            
            #nem um nem outro
            else:
                print('=-='*10)
                print("\nOpção inválida\n")
                print('=-='*10)
                cad = 4
        
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