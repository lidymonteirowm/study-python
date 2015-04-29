'''
14) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes 
maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa 
que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor 
da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
'''

peso = float(input('Peso:'))
if peso > 50:
	excedente = peso - 50
	multa = excedente * 4
else:
	excedente = 0
	multa = 0
print ('Peso: %.2f Kg' %peso)
print ('Excesso: %.2f Kg' %excedente)
print ('Multa: R$ %.2f' %multa)
