'''
15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.

'''

vh = float(input('Valor da hora:'))
qh = int(input('Quantidade de horas trabalhadas:'))

salario_bruto = vh * qh
inss = 8/100 * salario_bruto
sindicato = 5/100 * salario_bruto
ir = 11/100 * salario_bruto

salario_liquido = salario_bruto - inss - sindicato - ir

print (' + Salário Bruto: R$ %.2f' %salario_bruto)
print (' - IR: R$ %.2f' %ir)
print (' - INSS: R$ %.2f' %inss)
print (' - Sindicato: R$ %.2f' %sindicato)
print (' = Salário Liquido: R$ %.2f' %salario_liquido)
