import cadastro
print('=-='*10)
op = 0 
while True:
  op = int(input('1. Avaliação Física.\n2. Plano Alimentar.\n3. Avaliação física + Plano Alimentar.\n4. Sair\nEscolha uma opção: '))
  if op == 1:
    print('=-='*10)
    print('Avaliação Física custa R$50,00')
    print('Lista de nutricionistas disponíveis')
    quant = 0
    for i in cadastro.nutri_cadastrado:
      quant += 1
      print(quant,'. ',i['Nome'])
    select_nutri = int(input('Escolha uma opção (0 para Sair): '))
    if select_nutri > 0 and select_nutri<= len(cadastro.nutri_cadastrado):
      #pagamento
      print()
    elif select_nutri == 0:
      break
    else:
      print('Opção invalida!\nTente outra vez.\n')
  else:
    print('Opção invalida!\nTente outra vez.\n')
  print('=-='*10)

  