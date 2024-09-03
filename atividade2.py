produtos = {}

def  cadastro_produto(): 
  
  codigo = input("digite o codigo")
  nome = input("digite o nome")
  preco = float(input("digite o preco"))
  quantidade = int (input("digite a quantidade do estoque"))
  produtos[codigo]= {"nome":nome,"preço" : preco, "estoque" : quantidade}
  print ("PRODUTO CADASTRADO COM  SUCESSO")

def altera_preco():
    novo_preco = float(input("digite o novo preco"))
    codigo = input("entre com o codigo do produto")
    if(codigo in produtos):
      produtos[codigo]['preco'] = novo_preco
      print("preço alterado")
    
def pesquisa_produto():
    codigo = input("digite  o codigo do produto:")
    produtoencontrado = produtos.get(codigo)
    if produtoencontrado:
        print("produto encontrado")
        print(produtoencontrado)



while():
    print("Menu")
    print("1- Adicionar produto")
    print("2- alterar preço produto")
    print("3- pesquisar por codigo")
    print("------------------------")
    opcao = int(input("escolha por opçao"))
    if(opcao == 1):
        cadastro_produto()
    elif(opcao == 2):
        altera_peco()
    elif(opcao == 3):
        pesquisa_produto
    elif(opcao == 4):
        break
    else:
         print("escolha a opcao correta")


