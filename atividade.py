produtos = {}


while True:
  codigo = input("digitw o codigo do produto: ")
  nome = input("digite o nome do produto: ")
  preco = float(input("digite o preco de venda: "))
  quantidade = int(input("digite a quantidade"))
  produtos[codigo] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
  print("produto adicionado com  sucesso!")
  print(produtos)
  
  continuar = input ("continuar cadastrando")
 
 
  if continuar == ():
   if continuar.lower() == "não":
    break
print("fim")
  