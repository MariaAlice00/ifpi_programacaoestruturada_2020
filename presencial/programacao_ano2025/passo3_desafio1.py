print('Em que ano você nasceu?')
nascer = input()
nascer = int(nascer)

print('Para qual ano você quer saber sua idade?')
ano = input()
ano = int(ano)

idade = ano - nascer

print('No ano {} você terá {} anos!'.format(ano, idade))
