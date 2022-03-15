import math
import random
import pygame

# Retirando apenas a parte inteira de um número
num = float(input('Digite um número quebrado: '))
print('A parte inteira do número que você digitou é {}'.format(math.floor(num)))

# catetos e hipotenusa matematicamente e com módulo
adj = float(input('Digite o valor do cateto adjacente '))
opo = float(input('Digite o valor do cateto oposto '))
hip = (adj ** 2 + opo ** 2) ** (1 / 2)
hi = math.hypot(opo, adj)
print('A hipotenusa irá medir {:.2f} e {:.2f}'.format(hip, hi))

# Calculando Ângulo
ang = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}\n'
      'O ângulo de {} tem o COSSENO de {:.2f}\n'
      'O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, seno, ang, cose, ang, tang))

# Sorteio de informações
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
lista = [a, b, c, d]
escolhido = random.choice(lista)
print('O aluno escolhido foi o: {}'.format(escolhido))

# Sorteio de lista
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
lista = [a, b, c, d]
ordem = random.shuffle(lista)
print('A ordem será: {}'.format(ordem))

