dias = int(input('quantos dias vc andou: '))
km = float(input('quantos km voce andou: '))

cont = dias * 60 + km * 0.15

print('\033[4;33;45mtotal a pagar é de R$ {:.2f}\033[m'.format(cont))