pao_frances = int(input('Quantidade de pães franceses: ')) 
broa = int(input('Quantidade de broas: '))

pf = pao_frances * 0.12
b = broa * 1.50
total =  pf + b
poupanca = 0.10 * total

print('Você arrecadou R${:.2f}.\nE deve guardar R${:.2f} na sua poupança.'.format(total, poupanca))
