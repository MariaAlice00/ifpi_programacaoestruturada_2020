from random import *

macho = ['Akira', 'Alfredo', 'Duke', 'Hércules', 'Rambo', 'Thor']
femea = ['Ayza', 'Dara', 'Hope', 'Holly', 'Lady', 'Luna']

menu = 'Serviço de escolha de nome para animais de estimação\n' \
+ '-----------------------------------------------------\n' \
+ '1 - Obter nome\n' \
+ '2 - Adicionar nome\n' \
+ '3 - Remover nome\n' \
+ '4 - Imprimir nomes\n' \
+ '0 - Sair\n' \
+ 'Digite uma opção: '

opcao = int(input(menu))

while opcao != 0:
    if opcao == 1:
        qtd = int(input('De quantos nomes você precisa? '))
        for c in range(qtd):
            print('''
            Macho ou fêmea?
            m - macho
            f - fêmea
            ''')
            sexo = input('>>> ').lower()
            if sexo == 'm':
                print('Você deve chamar seu animal de estimação de', choice(macho))
            elif sexo == 'f':
                print('Você deve chamar seu animal de estimação de', choice(femea)) 
            else:
                print('Opção inválida')
 
    elif opcao == 2: # Adicionar nome
        print('''
        Macho ou fêmea?
        m - macho
        f - fêmea
        ''')
        sexo = input('>>> ').lower()
        if sexo == 'm':
            item_to_add = input('Adicione o nome: ')

            if item_to_add not in macho:
                macho.append(item_to_add)
            else:
                print('O nome já está na lista!')

        elif sexo == 'f':
            item_to_add = input('Adicione o nome: ')

            if item_to_add not in femea:
                femea.append(item_to_add)
            else:
                print('O nome já está na lista!')

        else:
            print('Opção inválida')
  
    elif opcao == 3: # Remover nome
        print('''
        Macho ou fêmea?
        m - macho
        f - fêmea
        ''')
        sexo = input('>>> ').lower()
        if sexo == 'm':
            item_to_delete = input('Remova o nome: ')

            if item_to_delete in macho:
                macho.remove(item_to_delete)
            else:
                print('O nome não está na lista!')

        elif sexo == 'f':
            item_to_delete = input('Remova o nome: ')

            if item_to_delete in femea:
                femea.remove(item_to_delete)
            else:
                print('O nome não está na lista!')

        else:
            print('Opção inválida')

    elif opcao == 4: # 4 - Imprimir nomes
        print('''
        Macho ou fêmea?
        m - macho
        f - fêmea
        ''')
        sexo = input('>>> ').lower()
        if sexo == 'm':
            print(macho)
        elif sexo == 'f':
            print(femea)
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')

    input('Continuar <enter> ...')
    opcao = int(input(menu))

print('Obrigado por usar nossos serviços!')
