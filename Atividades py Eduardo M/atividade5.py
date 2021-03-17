#5)Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
#(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = print(input('Digite o tipo de combustível que você colocou:'))
litro = print(input('Digite a quantidade de litros que você colocou:'))
desconto1 = int(input('3%'))
desconto2 = int(input('5%'))
desconto3 = int(input('4%'))
desconto4 = int(input('6%'))
if combustivel == "A":
   alcool = 3.5
   custo = litro * alcool
if litro <= 20:
   desconto1 = (custo * 3)/100
print("O desconto de combustivel foi de : {} e o preço agora é {}".format(desconto1,custo-desconto1))
if litro >= 20:
    desconto2 = (custo * 5)/100
print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto2,custo-desconto2))
if combustivel == "G":
    gasolina = 4.6
    custo = (litro * gasolina)
if litro <= 20:
   desconto3 = (custo * 4)/100
print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto3,custo-desconto3))
if litro > 20:
     desconto4 = (custo * 6)/100
print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto4,custo-desconto4))