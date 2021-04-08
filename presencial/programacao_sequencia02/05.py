h_normal = int(input('Quantas horas normais você trabalha? '))
h_extra = int(input('E quantas horas extras? '))

hora_normal = h_normal * 10
hora_extra = h_extra * 15
hora_total = hora_normal + hora_extra
salario_bruto = hora_total * 30
salario_liquido = salario_bruto - (0.10 * salario_bruto)

print('>>> Salário bruto: R$ {:.2f}'.format(salario_bruto))
print('>>> Salário líquido: R$ {:.2f}'.format(salario_liquido))