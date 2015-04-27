#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Km percorrido: '))
d = int(input('Quantidade de dias: '))
print('Valor a pagar por %d dias e %.2f Km: %.2f' %(d,km,(d*60 + 0.15*km)))