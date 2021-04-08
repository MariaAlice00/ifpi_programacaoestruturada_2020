sombra_predio = float(input('Tamanho da sombra do prédio: '))
sombra_usuario = float(input('Tamanho da sombra do usuário: '))
altura_usuario = float(input('Tamanho da altura do usuário: '))

altura_predio = (altura_usuario * sombra_predio) / sombra_usuario

print('A altura do prédio é de {:.2f}'.format(altura_predio))