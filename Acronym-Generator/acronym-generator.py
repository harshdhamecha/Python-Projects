def acronym(text):
    acr = ''
    for first_letter in text.split():
        acr += first_letter[0].upper()
    print(f'Acronym for {text}: {acr}')

text = input('Enter a text to see it\'s acronym: ')
acronym(text)