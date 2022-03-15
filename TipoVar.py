n1 = int(input('Digite um número: '))
a1 = (n1-1)
s1 = (n1+1)

print('O número que você escolheu foi {}, seu antecessor é {} e seu sucessor {}.'.format(n1, a1, s1))

n2 = int(input('Digite outro número: '))
d2 = (n2*2)
t2 = (n2*3)
rq2 = (n2**(1/2))

print('O número que você escolheu foi {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.0f}'.format(n2, d2, t2, rq2))

nt1 = int(input('Digite a primeira nota: '))
nt2 = int(input('Digite a segunda nota: '))
md = ((nt1+nt2)/2)

print('Suas notas foram:{} e {}, assim sua média final ficou:{:.2f}'.format(nt1, nt2, md))

vm = int(input('Insira um valor em metros: '))
cm = (vm*100)
mm = (vm*1000)

print('{} metros é equivalente a {} centímetro e {} milímetros'.format(vm, cm, mm))

ntab = int(input('Digite um número:'))
print('{} x {} = {}'.format(ntab, 1, ntab*1))
print('{} x {} = {}'.format(ntab, 2, ntab*2))
print('{} x {} = {}'.format(ntab, 3, ntab*3))
print('{} x {} = {}'.format(ntab, 4, ntab*4))
print('{} x {} = {}'.format(ntab, 5, ntab*5))
print('{} x {} = {}'.format(ntab, 6, ntab*6))
print('{} x {} = {}'.format(ntab, 7, ntab*7))
print('{} x {} = {}'.format(ntab, 8, ntab*8))
print('{} x {} = {}'.format(ntab, 9, ntab*9))
print('{} x {} = {}'.format(ntab, 10, ntab*10))

largura = float(input('Digite a largura da parede '))
altura = float(input('Digite a altura da parede '))
tamanho = largura * altura
print('A sua parede tem a dimensão de {}x{} e sua área é de {}m² '.format(largura, altura, tamanho))
tinta = tamanho / 2
print('para pintar essa parede você precisará de {} litros de tinta.'.format(tinta))

produto = float(input('Digite o preço do produto: '))
desconto = produto * 0.95
print('O produto com desconto de 5% ficará no valor de {:.2f}'.format(desconto))

salario = float(input('Digite o salário do funcionário: '))
reajuste = salario * 1.15
print('O salário do funcionário após o reajuste de 15% ficará {:.2f}'.format(reajuste))

celsius = float(input('Digite a temperatura em Celsius: '))
farenait = (celsius * 1.8) + 32
print('A temperatura de {:.2f}º Celsius será de {:.2f}º convertida para fairenait.'.format(celsius, farenait))

totaldias = int(input('Quantos dias você ficou com o carro? '))
totalkms = int(input('Quantos kms tu rodou com o carro? '))
precofinal = (totaldias*50)+(totalkms*3)
print('O valor do seu aluguel é de {}'.format(precofinal))


