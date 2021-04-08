n = int(input('Digite um número entre 100 e 999: '))
unidade = n % 10
n = n // 10
dezena = n % 10
n = n // 10
centena = n % 10
print(f'unidade: {unidade}, dezena: {dezena}, centena: {centena}.')
