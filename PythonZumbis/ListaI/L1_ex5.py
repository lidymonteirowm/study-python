#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

m = float(input('Preço mercadoria: '))
p = float(input('Porcentagem de desconto: '))
d = m * p / 100
preco = m - d
print('Desconto R$: %.2f ' %d)
print('Preço a pagar R$: %.2f' %preco)