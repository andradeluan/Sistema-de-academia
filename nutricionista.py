# funcionalidade Nutricionista

nome_nutricionistas = ['Nutri1','Nutri2','Nutri3','Nutri4','Nutri5'] #nomes dos Nutricionistas disponíveis 

opcao = 0 #variável que recebe a direção do aluno
while True: #laço de repetição menu nutrição
  opcao = int(input('1. Avaliação Física.\n2. Plano Alimentar.\n3. Avaliação física e Plano Alimentar.\n4. Sair\nSelecione a opção que você deseja: '))
  if opcao > 0 and opcao < 5:
    break
  else:
    print('Opção invalida!\nTente outra vez.\n')

if opcao == 1:# opção 1 Avaliação Física
  select_Nutri = 0
  print('Avaliação Física custa R$xx,xx')
  while True:
    select_Nutri = int(input(f'Selecione com qual nutricionista você deseja marcar sua Avaliação Física\n1. {nome_nutricionistas[0]}\n2. {nome_nutricionistas[1]}\n3. {nome_nutricionistas[2]}\n4. {nome_nutricionistas[3]}\n5. {nome_nutricionistas[4]}\n'))
    if select_Nutri > 0 and select_Nutri < 6:
      break
    else:
      print('Opção invalida!\nTente outra vez.\n')
elif opcao == 2:# opção 2 Plano Alimentar
  select_Nutri = 0
  print('Plano Alimentar custa R$yy,yy')
  while True:
    select_Nutri = int(input(f'Selecione com qual nutricionista você deseja para montar o seu Plano Alimentar.\n1. {nome_nutricionistas[0]}\n2. {nome_nutricionistas[1]}\n3. {nome_nutricionistas[2]}\n4. {nome_nutricionistas[3]}\n5. {nome_nutricionistas[4]}\n'))
    if select_Nutri > 0 and select_Nutri < 6:
      break
    else:
      print('Opção invalida!\nTente outra vez.\n')
elif opcao == 3:# opção 3 Plano Alimentar + Avaliação Física
  select_Nutri = 0
  print('Plano Alimentar + Avaliação Física custa R$yy,yy')
  while True:
    select_Nutri = int(input(f'Selecione com qual nutricionista você deseja para montar o seu Plano Alimentar e fazer sua Avaliação Física.\n1. {nome_nutricionistas[0]}\n2. {nome_nutricionistas[1]}\n3. {nome_nutricionistas[2]}\n4. {nome_nutricionistas[3]}\n5. {nome_nutricionistas[4]}\n'))
    if select_Nutri > 0 and select_Nutri < 6:
      break
    else:
      print('Opção invalida!\nTente outra vez.\n')
else:
  print('menu principal')#'voltar' ao menu principal