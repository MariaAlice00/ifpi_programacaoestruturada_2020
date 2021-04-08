distancia = float(input('Que distância deseja percorrer em km: '))

if distancia <= 200:
    print('Preço da passagem: R$ {:.2f}'.format(0.50 * distancia))
else:
    print('Preço da passagem: R$ {:.2f}'.format(0.45 * distancia))

