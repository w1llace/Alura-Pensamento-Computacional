preco_hamburger = 12
preco_batata = 7
preco_refri = 5

qtd_hamburger = int(input("Digite a quantidade de hambúrgueres: "))
qtd_batata = int(input("Digite a quantidade de batatas fritas: "))
qtd_refri = int(input("Digite a quantidade de refrigerantes: "))

total_hamburger = preco_hamburger * qtd_hamburger
total_batata = preco_batata * qtd_batata
total_refri = preco_refri * qtd_refri

total_pedido = total_hamburger + total_batata + total_refri

print(f"Total do pedido: R$ {total_pedido}")