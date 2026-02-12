total = 0

despesa = float(input("Digite o valor das despesas (0 para sair): "))

while despesa != 0:
    total += despesa
    despesa = float(input("Digite o valor das despesas (0 para sair): "))

print("O valor total das despesas é:", total)