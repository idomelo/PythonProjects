from random import randint

# Definindo listaInscrições e inscrição como vazios
listaInscrições = []
inscrição = {}

# Enquanto usuário não escolher '0', o menu continua a aparecer
escolha = ''
while escolha != '0':
    print('*'*10 + 'MENU' + '*'*10)
    print('1 - Nova inscrição\n'
          '2 - Visualizar Inscrição\n'
          '0 - Encerrar\n')

    escolha = input('Opção escolhida:')

    # Se opção escolhida não constar no menu, exibir erro e retornar ao início do loop
    if escolha != '1' and escolha != '2' and escolha != '0':
        print('\nErro: digite uma opção válida!\n')
        continue

    # Se a opção 1 for escolhida, adicionar entradas ao dicionário 'inscrição'
    if escolha == '1':
        inscrição['nome'] = input('Digite seu nome:')
        inscrição['email'] = input('Digite e-mail:')
        inscrição['telefone'] = input('Digite telefone:')
        inscrição['curso'] = input('Curso escolhido:')
        # Gerando voucher aleatório
        inscrição['voucher'] = randint(100, 400)

        # Adicionar cópia do dicionário inscrição à listaInscrições
        listaInscrições.append(inscrição.copy())

    # Se a opção 2 for escolhida, verifica se contém dados.
    if escolha == '2':
        if listaInscrições:
            print('-'*15 + 'LISTA DE INSCRITOS' + '-'*15 + '\n')

            # Formatação do dicionário para apresentar chave e valor
            # Para cada dicionario 'p' dentro de listaInscrições, pegar cada chave e valor, formatando-os.
            for p in listaInscrições:
                for i, j in p.items():
                    print('{} : {}'.format(i, j))

        # Se não houver dados, exibir mensagem de erro
        else:
            print('\nErro: Nenhuma inscrição cadastrada!\n')

print('Encerrando programa ...')
exit()
