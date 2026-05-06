produtos = {'produto1': 10.99, 'produto2': 5.49, 'produto3': 20.00 }
desconto = 0.1
for itens in produtos.values():
  preco_novo =  itens - (itens * desconto)
  print(preco_novo) #aplica um desconto de 10% em cada preço dos produtos e printa os novos preços com desconto