def nutri():
  import cadastro
  import pagamento
  print('=-='*10)
  op = 0 
  while True:
    op = int(input('1. Avaliação Física.\n2. Plano Alimentar.\n3. Avaliação física + Plano Alimentar.\n4. Sair\nEscolha uma opção: '))
    if op == 1:
      print('=-='*10)
      print('\nAvaliação Física custa R$50,00\n')
      print('=-='*10)
      print('\nLista de nutricionistas disponíveis:\n')
      quant = 0
      for i in cadastro.nutri_cadastrado:
        quant += 1
        print(quant,'. ',i['nome'])
        print('=-='*10)
      select_nutri = int(input('Escolha uma opção (0 para Sair): '))
      if select_nutri > 0 and select_nutri<= len(cadastro.nutri_cadastrado):
        plano = "Avaliação Física", 50.00, 1
        sucesso_pagamento = pagamento.escolher_forma_de_pagamento(plano)
        if sucesso_pagamento == True:
          print('Consulta marcada com sucesso')
      elif select_nutri == 0:
        break
      else:
        print('Opção invalida!\nTente outra vez.\n')
    elif op == 2:
      print('=-='*10)
      print('Plano Alimentar custa R$150,00')
      print('Lista de nutricionistas disponíveis')
      quant = 0
      for i in cadastro.nutri_cadastrado:
        quant += 1
        print(quant,'. ',i['nome'])
      select_nutri = int(input('Escolha uma opção (0 para Sair): '))
      if select_nutri > 0 and select_nutri<= len(cadastro.nutri_cadastrado):
        plano = "Plano Alimentar", 150.00, 3
        sucesso_pagamento = pagamento.escolher_forma_de_pagamento(plano)
        if sucesso_pagamento == True:
          print('Consulta marcada com sucesso')
      elif select_nutri == 0:
        break
      else:
        print('Opção invalida!\nTente outra vez.\n')
    elif op == 3:
      print('=-='*10)
      print('Avaliação física + Plano Alimentar custa R$150,00')
      print('Lista de nutricionistas disponíveis')
      quant = 0
      for i in cadastro.nutri_cadastrado:
        quant += 1
        print(quant,'. ',i['nome'])
      select_nutri = int(input('Escolha uma opção (0 para Sair): '))
      if select_nutri > 0 and select_nutri<= len(cadastro.nutri_cadastrado):
        plano = "Avaliação física + Plano Alimentar", 150.00, 3
        sucesso_pagamento = pagamento.escolher_forma_de_pagamento(plano)
        if sucesso_pagamento == True:
          print('Consulta marcada com sucesso')
      elif select_nutri == 0:
        break
      else:
        print('Opção invalida!\nTente outra vez.\n')
    elif op == 4:
      break
    else:
      print('Opção invalida!\nTente outra vez.\n')
    print('=-='*10)

  