#4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

s = float(input('Valor do Salário: '))
p = float(input('Porcentagem de aumento %: '))
aum = s * p /100
ns = s + aum
print('Aumento: R$ %.2f ' %aum)
print('Novo Salário: R$ %.2f' %ns)