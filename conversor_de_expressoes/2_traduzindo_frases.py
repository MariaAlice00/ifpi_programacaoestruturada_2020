text_speak_dictionary = {
    'rs':'risos',
    'tbm':'também',
    'vc':'você',
    'pq':'porque',
    'blz':'beleza'
}

sentence = input('Insira uma frase para traduzir: ').lower()

words_to_translate = sentence.split() # divide a frase em uma lista de palavras
translated_sentence = ''

for word in words_to_translate:
    if word in text_speak_dictionary:
        translated_sentence += text_speak_dictionary[word] + ' '
    else:
        translated_sentence += word + ' '

print('==>')
print(translated_sentence)