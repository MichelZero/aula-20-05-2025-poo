#
# autor: Michel
# data: 2025/05/20

#
# 2.Agrupamento por Categoria:
# Problema: Você tem uma lista de itens, onde cada item
# é um dicionário com um campo "categoria". 
# Crie um dicionário onde as chaves são as 
# categorias e os valores são listas de itens 
# pertencentes a cada categoria.
# Exemplo:


# Saída esperada: {
  #   'Fruta': [{'nome': 'Maçã', 'categoria': 'Fruta'},
  #             {'nome': 'Banana', 'categoria': 'Fruta'}],
  # 'Vegetal': [{'nome': 'Cenoura', 'categoria': 'Vegetal'},
  #             {'nome': 'Alface', 'categoria': 'Vegetal'}]}

lista = [
    {"nome": "Maçã", "categoria": "Fruta"}, # Item 1, tipo DIC
    {"nome": "Banana", "categoria": "Fruta"}, # Item 2
    {"nome": "Cenoura", "categoria": "Vegetal"}, # Item 3
    {"nome": "Alface", "categoria": "Vegetal"}, # Item 4
]


""" for item in lista: # percorre a lista de dicionários 
  #print(item) # imprime o dicionário
  qqnome = item['nome'] # acessa o valor da chave 'nome' do dicionário 
  print(qqnome) """

categorias = {}   # dicionário vazio 
for item in lista:  # percorre a lista de dicionários, item é o nome da variável que vai receber cada dicionário
  # print(item) # imprime o dicionário
  qqnome = item['categoria'] # acessa o valor da chave 'categoria' do dicionário 
  if qqnome in categorias:  # verifica se a categoria já está no dicionário, qqnome é a chave
    # print(qqnome) # imprime o valor da chave 'categoria'
    categorias[qqnome].append(item)  # se já estiver, adiciona o item à lista da categoria 
  else:
    categorias[qqnome] = [item]  # se não estiver, cria uma nova lista com o item 
    
# saida
print(categorias) 