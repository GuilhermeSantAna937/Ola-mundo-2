condicao = True

while condicao:
    nome = input('Qual o seu nome: ')

    if nome == 'sair':
        break # para a execução do while, sai logo de repetição 

    print(f'Seu nome é {nome}')

    print('Acabou')
