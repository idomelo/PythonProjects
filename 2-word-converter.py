# Entrada do nome a ser convertido
userName = input('Digite um nome:')

# Transformando a string 'userName' em uma lista (para torná-la mutável) e tornando maiúsculas as letras
userNameLi = list(userName.upper())

# Para cada item(letter) da lista, verificar se corresponde a vogal determinada
for letter in userNameLi:
    if letter in 'A':    # Se o item(letter) for a vogal, substituir o item da lista pelo símbolo correspondente
        userNameLi[userNameLi.index('A')] = '@'
    if letter in 'E':
        userNameLi[userNameLi.index('E')] = '&'
    if letter in 'I':
        userNameLi[userNameLi.index('I')] = '!'
    if letter in 'O':
        userNameLi[userNameLi.index('O')] = '#'
    if letter in 'U':
        userNameLi[userNameLi.index('U')] = '*'

# Printando palavra completa
print(userName.upper())

# Utilizando '.join' para reagrupar todos os itens da lista e formar a palavra
print("".join(userNameLi))
