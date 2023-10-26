# from datetime import datetime, timedelta
def escolher_plano():
    print('=-='*10)
    print("\nEscolha um plano:\n")
    print("[ 1 ] Mensal - Valor: R$100,00 (até 1x)")
    print("[ 2 ] Trimestral - Valor: R$270,00 (até 3x de R$90,00)")
    print("[ 3 ] Semestral - Valor: R$420,00 (até 6x de R$70,00)")
    print("[ 4 ] Anual - Valor: R$600,00 (até 12x de R$50,00)\n")
    print('=-='*10)

    escolha = int(input("\nEscolha o número do plano desejado: "))

    if escolha == 1:
        return "Mensal", 100.00, 1
    elif escolha == 2:
        return "Trimestral", 270.00, 3
    elif escolha == 3:
        return "Semestral", 420.00, 6
    elif escolha == 4:
        return "Anual", 600.00, 12
    else:
        return None


def escolher_forma_de_pagamento(plano):
    print('=-='*10)
    print("\nEscolha a forma de pagamento:\n")
    print("[ 1 ] Pix")
    print("[ 2 ] Dinheiro")
    print("[ 3 ]Cartão de Crédito")
    print("[ 4 ]Cartão de Débito\n")
    print('=-='*10)

    escolha = int(input("\nEscolha o número da forma de pagamento desejada: "))

    if escolha == 1:
        print('=-='*10)
        print("\nAguarde enquanto geramos o QR code para pagamento\n")
        print('=-='*10)
        # Simular pagamento bem-sucedido
        print("\nPagamento realizado com sucesso\n")
        print('=-='*10)
        return True
    elif escolha == 2:
        print('=-='*10)
        print("\nTransação autorizada\n")
        print('=-='*10)
        return True
    elif escolha == 3:
        max_parcelas = plano[2]
        print('=-='*10)
        parcelas = int(input(f"\nEscolha o número de parcelas (até {max_parcelas}): "))
        print('=-='*10)
        if 1 <= parcelas <= max_parcelas:
            print('=-='*10)
            print(f"\nTransação autorizada para {parcelas} parcelas\n")
            print('=-='*10)
            return True
        else:
            print('=-='*10)
            print("\nNúmero de parcelas inválido para o plano escolhido\n")
            print('=-='*10)
    elif escolha == 4:
        print('=-='*10)
        print("\nTransação autorizada\n")
        print('=-='*10)
        return True
    else:
        print('=-='*10)
        print("\nOpção de pagamento inválida\n")
        print('=-='*10)

    return False


#def adicionar_status_do_plano(plano, parcelas):
#    hoje = datetime.now()
#   data_do_pagamento = hoje.strftime("%d/%m/%Y")
#   data_do_plano = hoje + timedelta(days=30 * parcelas)
#   data_do_plano = data_do_plano.strftime("%d/%m/%Y")

#   print("Status do plano do aluno:")
#   print(f"Plano: {plano[0]}")
#   print("Situação: Ativo")
#   print(f"Início: {data_do_pagamento}")
#   print(f"Validade: {data_do_plano}")


#plano = escolher_plano()
#if plano:
#    sucesso_pagamento = escolher_forma_de_pagamento(plano)
#    if sucesso_pagamento:
#        adicionar_status_do_plano(plano, plano[2])
#else:
#    print("Opção de plano inválida.")

