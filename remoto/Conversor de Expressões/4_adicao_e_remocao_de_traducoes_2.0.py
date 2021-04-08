def display_menu():
    print('trdtr de exprss')
    print('='* 13)
    print('Menu:')
    print(' c = converter uma frase')
    print(' p = imprimir dicionário')
    print(' a = adicionar uma palavra')
    print(' d = remover uma palavra')
    print(' q = sair')


def convert_sentence():
    sentence = input('Insira uma frase para traduzir: ').lower()
    translated_sentence = ''

    list_of_words = sentence.split()

    for word in list_of_words:
        if word in text_speak_dictionary:
            translated_sentence += text_speak_dictionary[word] + ' '
        else:
            translated_sentence += word + ' '

    print('==>')
    print(translated_sentence)


def add_dictionary_item():
    txt_to_add = input('Insira a expressão a ser adicionada ao dicionário: ')

    if txt_to_add not in text_speak_dictionary:
        meaning = input('O que ela significa? ')

        text_speak_dictionary[txt_to_add] = meaning
    else:
        print('Essa expressão já está no dicionário!')


def delete_dictionary_item():
    txt_to_delete = input('Insira a expressão a ser removida ao dicionário: ')

    if txt_to_delete in text_speak_dictionary:    
        del text_speak_dictionary[txt_to_delete]
    else:
        print('Essa expressão não existe no dicionário!')


text_speak_dictionary = {
    'rs':'risos',
    'tbm':'também',
    'vc':'você',
    'pq':'porque',
}
 
running = True

display_menu()

while running == True:
    menu_choice = input('> ').lower()

    if menu_choice == 'c':
        convert_sentence()
    elif menu_choice == 'p':
        print(text_speak_dictionary)
    elif menu_choice == 'a':
        add_dictionary_item()
    elif menu_choice == 'd':
        delete_dictionary_item()
    elif menu_choice == 'q':
        running = False
    else:
        print('Escolha inválida!')