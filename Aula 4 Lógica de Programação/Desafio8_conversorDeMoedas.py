taxa_de_cambio = 5.22 #valor atual do dolar em reais

moedasReais = float(input('Digite a quantidade em R$: '))
moedasDolar = (moedasReais/taxa_de_cambio)

print("A quantidade em Dolar é: $", moedasDolar)