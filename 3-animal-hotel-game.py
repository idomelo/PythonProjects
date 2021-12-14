# Instruções iniciais:
print('\n   HOTEL DOS ANIMAIS\n'
      'Especificando a posição:\n')

# Declarando matriz position como exemplo para o jogador
position = [[1, 2, 3, 4], [5, 6, 7, 8]]

# Mostrando na tela os elementos da matriz
# (para cada linha e cada coluna, exibir elemento de índice[linha][coluna])
for l in range(0, 2):
    for c in range(0, 4):
        print(f'[{position[l][c]:^2}]', end='')
    print()
print('\n')


# Fase 1 #


print('Bem vindo à fase 1!\n'
      'Na fase 1, o jogador deve alocar o GATO e o RATO na seguinte matriz que representa os quartos:\n'
      'Quartos com "*" estão bloqueados.')

# Declarando matriz da fase 1
fase1 = [['*', '*', '__', 'G'], ['R', '__', '*', '*']]

# Mostrando elementos da matriz na tela
for l in range(0, 2):
    for c in range(0, 4):
        print(f'[{fase1[l][c]:^2}]', end='')
    print()

# Solicitando resposta do jogador
respostaGato = input('Em qual posição colocar o GATO?')
respostaRato = input('Em qual posição colocar o RATO?')

# Verificando a resposta
if respostaGato == '3' and respostaRato == '6':
    print('\nParabéns, vamos para a fase 2:')
else:
    print('\nVocê perdeu!')
    exit()


# Fase 2 #


print('Agora, você deve alocar 2 CÃES e 1 OSSO:')

# Declarando matriz da fase 2
fase2 = [['__', '*', '*', '*'], ['*', 'C', '__', '__']]

# Mostrando elementos da matriz na tela
for l in range(0, 2):
    for c in range(0, 4):
        print(f'[{fase2[l][c]:^2}]', end='')
    print()

# Solicitando resposta do jogador
respostaCao1 = input('Em qual posição colocar o CÃO N°1?')
respostaCao2 = input('Em qual posição colocar o CÃO N°2?')
respostaOsso = input('Em qual posição colocar o OSSO?')

# Verificando a resposta

# Verifico se o jogador colocou o cão 1 e o cão 2 em quartos diferentes(Há 2 respostas possíveis)
# e também se as demais respostas estão corretas
if (respostaCao1 != respostaCao2) and (respostaCao1 == '7' or '8') and (respostaCao2 == '7' or '8') and (
        respostaOsso == '1'):
    print('\nParabéns, vamos para a fase 3:')
else:
    print('Você perdeu!')
    exit()


# Fase 3 #


print('Agora, você deve alocar 1 GATO, 1 RATO e 1 OSSO :')

# Declarando matriz da fase 3
fase3 = [['__', '*', '*', '*'], ['__', 'G', '__', '*']]

# Mostrando elementos da matriz na tela
for l in range(0, 2):
    for c in range(0, 4):
        print(f'[{fase3[l][c]:^2}]', end='')
    print()

# Solicitando resposta do jogador
respostaGato2 = input('Em qual posição colocar o GATO?')
respostaRato2 = input('Em qual posição colocar o RATO?')
respostaOsso2 = input('Em qual posição colocar o OSSO?')

# Verificando se o jogador colocou o gato e o osso em quartos diferentes
# E se as demais respostas estão corretas
if (respostaGato2 != respostaOsso2) and (respostaGato2 == '5' or '7') and (respostaOsso2 == '5' or '7') and (
        respostaRato2 == '1'):
    print('\nParabéns, vamos para a fase 4:')
else:
    print('Você perdeu!')
    exit()


# Fase 4 #


print('Agora, você deve alocar 2 QUEIJOS e 1 OSSO:')

# Declarando matriz da fase 4
fase4 = [['__', '__', '__', '*'], ['*', 'R', '*', '*']]

# Mostrando elementos da matriz na tela
for l in range(0, 2):
    for c in range(0, 4):
        print(f'[{fase4[l][c]:^2}]', end='')
    print()

# Solicitando resposta do jogador
respostaQueijo1 = input('Em qual posição colocar o QUEIJO n°1?')
respostaQueijo2 = input('Em qual posição colocar o QUEIJO n°2?')
respostaOsso3 = input('Em qual posição colocar o OSSO?')

# Verificando se o jogador colocou o gato e o osso em quartos diferentes
# E se as demais respostas estão corretas
if (respostaQueijo1 != respostaQueijo2) and (respostaQueijo1 == '1' or '3') and (respostaQueijo2 == '1' or '3') and (
        respostaOsso3 == '2'):
    print('\nVOCÊ GANHOU!!')
else:
    print('Você perdeu!')
    exit()
