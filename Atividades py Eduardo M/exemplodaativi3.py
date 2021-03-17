#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

valor1 = int(input('insira o primeiro valor: '))
valor2 = int(input('insira o segundo valor: '))

print('o que voce quer fazer?')
opcao = int(input('1 - Adicao\n2 - Subtracao\n3- Multiplicacao\n4 - Divisao'))

if opcao == 1:
    resultado = valor + valor2
elif opcao == 2:
    resultado = valor1 - valor2
elif opcao == 3:
    resultado = valor1 * valor2
elif opcao == 4:
    resultado = valor1 / valor2
else:
    print('opcao invalida')
    exit()

print('Resultado = ', resultado)

if resultado % 2 == 0:
    print('numero par')
else:
    print('numero impar')

if resultado >= 0:
    print('numero possitivo')
else:
    print('Numero negativo')

if type(resultado) == "<class 'int'>":
    print('numero inteiro')
else:
    print('numero decimal')