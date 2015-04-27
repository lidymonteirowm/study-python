#10)Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros_dia = int(input('Cigarros por dia: '))
anos = int(input('Anos de fumante: '))


'''Quantos cigarros equivale a um dia 
1dia = 1440 minutos
10 min = 1cigarro
1440/10 = 144

1 dia = 1440 minutos =  144 cigarros_dia 

total_cigarros = anos * 365 * cigarros_dia
total_dias_perdidos = total_cigarros/144
'''

total_cigarros = anos * 365 * cigarros_dia
total_dias_perdidos = total_cigarros / 144
print('%d cigarros fumados em %d anos equivale a %2.f dias dias a menos!' %(total_cigarros, anos, total_dias_perdidos))
