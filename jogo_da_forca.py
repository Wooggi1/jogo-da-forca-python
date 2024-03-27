print('*****************Forca*****************')

palavra_reservada = 'Brasil'
palavra_reservada_lower = palavra_reservada.lower() 
lista_palavra = ['_' if letra != ' ' else ' ' for letra in palavra_reservada]
limite = 0
lista_boneco = [' o\n', '/', '|', '\\ \n', '/', ' \\']

while limite < len(lista_boneco):
    for letra in lista_palavra:
        print(letra, end=' ')

    print('\n')

    chute = input('Digite a letra: ').lower()

    if chute not in palavra_reservada_lower:
        print('Tente de novo')
        limite += 1
        print(''.join(lista_boneco[:limite]))
        continue
    
    for i, letra in enumerate(palavra_reservada_lower):
        if letra == chute:
            lista_palavra[i] = palavra_reservada[i]

    if palavra_reservada_lower == ''.join(letra.lower() for letra in lista_palavra):
        print('ggez')
        print(f'resposta: {"".join(lista_palavra)}')
        break

if limite == len(lista_boneco):
    print('perdeu D:')
