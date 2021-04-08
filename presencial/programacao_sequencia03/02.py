custo_fabrica = float(input('Digite o custo de fábrica: '))

distribuidor = 0.28 * custo_fabrica
imposto = 0.45 * custo_fabrica
custo_consumidor = custo_fabrica + distribuidor + imposto

print('O custo do carro novo é de R$ {:.2f}'.format(custo_consumidor))