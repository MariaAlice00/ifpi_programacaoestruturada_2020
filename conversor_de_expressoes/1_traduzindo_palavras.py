text_speak_dictionary = {
    'rs':'risos',
    'tbm':'também'
}

print('Dicionário =', text_speak_dictionary) # imprimir o dicionário inteiro

print('\nrs=', text_speak_dictionary['rs']) # imprimir apenas o conteúdo relacionado à chave 'rs

key = input('\nO que você gostaria de converter? ') # texto que pede a entrada do usuário
print(key, '=', text_speak_dictionary[key])
