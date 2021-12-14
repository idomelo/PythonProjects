# O laço while permanece ativo até que o usuário selecione 'break' no final
while True:
    # Entrada de dados
    nome = input('\nNome da criança:')

    # Se o usuário deixar 'idade' vazio, é atribuído o valor zero à variável, evitando "valueError"
    try:
        idade = int(input('Idade:'))
    except ValueError:
        idade = 0

    # Enquanto uma das inputs estiver vazia, retornar pedido de preenchimento ao usuário
    while nome == '' or idade < 1:
        print('Digite os dados corretamente.')
        nome = input('Nome da criança:')
        try:
            idade = int(input('Idade:'))
        except ValueError:
            idade = 0

    # Definindo a escolaridade de acordo com a Idade

    escolaridade = ''
    if 1 <= idade < 6:
        escolaridade = 'ensino infantil'
    elif 6 <= idade < 11:
        escolaridade = 'ensino fundamental I'
    elif 11 <= idade < 15:
        escolaridade = 'ensino fundamental II'
    elif idade >= 15:
        escolaridade = 'ensino médio'

    # Definindo a mensagem final
    print('O(a) Aluno(a) {} tem {} anos e está no {}'.format(nome, idade, escolaridade))

    # Usuário Seleciona 1 para continuar ou 0 para sair do loop
    DesejaContinuar = input('Deseja continuar? 0 - não      1 - sim')
    if DesejaContinuar == '0':
        break
    elif DesejaContinuar == '1':
        continue

print('\nEncerrando o programa ...')
