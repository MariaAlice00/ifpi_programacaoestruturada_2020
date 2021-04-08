salario = float(input('Salário do funcionário: R$ '))

if salario > 1250:
    print('Salário com aumento: R$ {:.2f}'.format(salario + (0.1 * salario)))
if salario <= 1250:
    print('Salário com aumento: R$ {:.2f}'.format(salario + (0.15 * salario)))

