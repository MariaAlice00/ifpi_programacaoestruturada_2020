dias = int(input('Quantidade de dias alugados: '))
km = float(input('Quantos km foram percorridos: '))
total = (dias * 60) + (km * 0.15)
print(f'O total a pagar pelo aluguel é de R$ {total:.2f}')
