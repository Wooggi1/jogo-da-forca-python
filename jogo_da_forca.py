print('*****************Forca*****************')

palavra_reservada = 'Brasil'
lista_palavra = ['_' for x in range(len(palavra_reservada))]
limite = 0
lista_boneco = [' o\n', '/', '|', '\\ \n', '/', ' \\']

while(limite < len(lista_boneco)):
    for letra in lista_palavra:
        print(letra, end=' ')

    print('\n')

    chute = input('Digite a letra: ')

    if chute not in palavra_reservada:
        print('Tente de novo')
        limite += 1
        print(''.join(lista_boneco[:limite]))
        continue
    
    for i, letra in enumerate(palavra_reservada):
        if letra == chute:
            lista_palavra[i] = chute

    if palavra_reservada == ''.join(lista_palavra):
        print('ggez')
        print(f'resposta: {''.join(lista_palavra)}')
        break

if limite == len(lista_boneco):
    print('perdeu D:')