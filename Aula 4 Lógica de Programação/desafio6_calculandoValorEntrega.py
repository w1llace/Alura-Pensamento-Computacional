'''
entrega_5km = 5
entrega_5km_10km = 8
entrega_10km_mais = 10

chuva = 2
'''

distancia = float(input("Digite a distância em km para entrega: "))
esta_chovendo = input('Está chovendo? (s/n): ')

if distancia <= 5:
    valorEntrega = 5
elif distancia <= 10:
    valorEntrega = 8
else:
    valorEntrega = 10

if esta_chovendo == 's' or esta_chovendo == 'Sim' or esta_chovendo == 'sim':
    valorEntrega += 2 #adiciona o valor da chuva ao valor da entrega
else:
    valorEntrega += 0

print(f"O valor total da entrega é: R$ {valorEntrega}") #usando f-string para formatar a saída do valor da entrega