nome = str(input('Digite o seu nome completo: '))
print('O seu nome com letras maiusculas ficaria {}'.format(nome.upper()))
print('O seu nome com letras minusculas ficaria {}'.format(nome.lower()))
print('O seu nome tem um total de {} letras'.format(len(nome.replace(' ', ''))))
pnome = nome.split()
print('O seu primeiro é {} nome tem {} letras'.format(pnome[0], len(pnome[0])))