nome = str(input('Digite seu nome completo: '))
pnome = nome.split()
print('Seu primeiro nome: {}\n'
      'Seu último nome: {}'
      .format(pnome[0],pnome[-1]))