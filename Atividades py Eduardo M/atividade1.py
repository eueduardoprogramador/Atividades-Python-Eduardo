#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo

numero = float(input('Informe um numero inteiro:'))
resultado = numero % 2
if resultado == 0:
    print('o numero e par'.format (numero))
else:
    print('numero e impar'.fotmat (numero))


