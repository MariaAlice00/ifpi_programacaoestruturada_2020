a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))

if a > b and a > c and b < a and b < c:
    print(f'O maior número é: {a}')
    print(f'O menor número é: {b}')
if a > b and a > c and c < a and c < b:
    print(f'O maior número é: {a}')
    print(f'O menor número é: {c}')
if b > a and b > c and a < b and a < c:
    print(f'O maior número é: {b}')
    print(f'O menor número é: {a}')
if b > a and b > c and c < a and c < b:
    print(f'O maior número é: {b}')
    print(f'O menor número é: {c}')
if c > a and c > b and a < b and a < c:
    print(f'O maior número é: {c}')
    print(f'O menor número é: {a}')
if c > a and c > b and b < a and b < c:
    print(f'O maior número é: {c}')
    print(f'O menor número é: {b}')




