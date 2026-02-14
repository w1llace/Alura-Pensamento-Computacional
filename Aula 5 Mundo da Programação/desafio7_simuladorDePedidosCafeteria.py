
itens = int(input("Quantos itens você deseja pedir? "))

qtd_itens = itens

valorTotal = 0

for i in range(qtd_itens): # o loop irá se repetir a quantidade de vezes igual ao número de itens que o cliente deseja pedir
    nome_item = input("Digite o nome do item: ")
    preco_item = float(input("Digite o preço do item: R$ "))

    valorTotal += preco_item # acumulando o valor total dos itens com o operador de atribuição +=

print("Você é um cliente cadastrado? (sim/não) ")
cliente_cadastrado = input().lower() #lower converte a resposta para minúscula para facilitar a comparação

if cliente_cadastrado == "sim" or cliente_cadastrado == "s":
    print("Você tem direito a um desconto de 10%!")
    
    #total = valorTotal*0.90 # aplicando diretamente o desconto de 10% multiplicando o valor total por 0.90 (100% - 10% = 90% = 0.90)
    
    #OU

    valorDesconto = valorTotal*0.10 # x*0.10 = 10% do valor total é o desconto
    total = valorTotal - valorDesconto
else:
    print("Você não tem direito a desconto.")
    total = valorTotal

print(f"\nO total a pagar é: R$ {total:.2f}")

