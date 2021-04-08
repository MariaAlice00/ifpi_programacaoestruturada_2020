senha_dicionario = {
    'alice':'alice123',
    'sol':'ols0'
}

print('Programa super secreto')
print('='* 15)

login_attempts = 0

while login_attempts < 3:
    nome = input('Nome: ')
    senha = input('Senha: ')

    if nome in senha_dicionario and senha == senha_dicionario[nome]:
        print('BEM-VINDO', nome.upper())
    else:
        print('ACESSO NEGADO')
        login_attempts += 1
    

print('Fim de serviço!')