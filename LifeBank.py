print('==' * 16)
print('{:^30}'.format('LIFE BANK'))
print('==' * 16)
valor = int(input('Quanto você quer sacar? R$'))
saque = cont50 = cont20 = cont10 = cont05 = cont02 = cont01 = 0
while True:
    while not valor - saque < 50:
        saque += 50
        cont50 += 1
    while not valor - saque < 20:
        saque += 20
        cont20 += 1
    while not valor - saque < 10:
        saque += 10
        cont10 += 1
    while not valor - saque < 5:
        saque += 5
        cont05 += 1
    while not valor - saque < 2:
        saque += 2
        cont02 += 1
    while not valor - saque < 1:
        saque += 1
        cont01 += 1
    if saque == valor:
        break

if cont50 != 0:
    print(f'{cont50} cédulas de R$50')
if cont20 != 0:
    print(f'{cont20} cédulas de R$20')
if cont10 != 0:
    print(f'{cont10} cédulas de R$10')
if cont05 != 0:
    print(f'{cont05} cédulas de R$5')
if cont02 != 0:
    print(f'{cont02} cédulas de R$2')
if cont01 != 0:
    print(f'{cont01} cédulas de R$1')
print('OPERAÇÃO FINALIZADA')
