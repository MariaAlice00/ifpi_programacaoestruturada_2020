lata350 = int(input('Quantas latas de 350 ml você comprou? '))
garrafa600 = int(input('E quantas garrafas de 600 ml? '))
garrafa2 = int(input('E quantas garrafas de 2 litros? '))

l_350_ml = lata350 * 350
l_350_l = l_350_ml / 1000
g_600_ml = garrafa600 * 600
g_600_l = g_600_ml / 1000
g_2_l = garrafa2 * 2
total = l_350_l + g_600_l + g_2_l

print('Você comprou {} litros de refrigerante!!!'.format(total))