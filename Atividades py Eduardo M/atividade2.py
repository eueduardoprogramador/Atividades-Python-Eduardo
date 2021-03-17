#Faça um programa que peça um numero e informe se o numero é inteiro ou decimal

num = float(input('informe um numero: '))
if int(num) == num:
     print('numero inteiro:')
else:
     print('numero decimal:')