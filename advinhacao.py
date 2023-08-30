from random import randint

a = randint(0,5)

print(a)

num = int(input('digite o seu numero: '))
if num == a:
    print('Parabens voce acertou!')
else:
    print('Tente novamente')