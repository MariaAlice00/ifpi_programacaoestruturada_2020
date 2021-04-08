um = int(input('Quantidade de moedas de 1 centavo: '))
cinco = int(input('Quantidade de moedas de 5 centavos: '))
dez = int(input('Quantidade de moedas de 10 centavos: '))
vinte_e_cinco = int(input('Quantidade de moedas de 25 centavos: '))
cinquenta = int(input('Quantidade de moedas de 50 centavos: '))
um_real = int(input('Quantidade de moedas de 1 real: '))

q_um = um * 1
q_cinco = cinco * 5
q_dez = dez * 10
q_vinte_e_cinco = vinte_e_cinco * 25
q_cinquenta = cinquenta * 50
centavo_real = (q_um + q_cinco + q_dez + q_vinte_e_cinco + q_cinquenta) / 10
um_real_total = um_real * 1
total = centavo_real + um_real_total

print('Você conseguiu economizar R$ {:.2f}'.format(total))