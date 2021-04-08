velocidade = float(input('Velocidade do carro em km/h: '))

if velocidade > 80:
    print('Você foi multado!')
    print('Valor da multa: R$ {:.2f}'.format((velocidade - 80) * 5))
if velocidade <= 80:
    print('Você está dentro do limite de velocidade!')