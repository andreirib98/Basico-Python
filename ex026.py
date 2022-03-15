frase = str(input('Digite uma frase da sua escolha: '))
print('A letra "A" aparece {} vezes\n'
      'A primeira vez que ela aparece é na posição {}\n'
      'E a ultima vez que ela aparece é na posição {}'
      .format(frase.upper().count('A'), ))