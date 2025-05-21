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
  #        'Fruta': [{'nome': 'Maçã'},
  #                  {'nome': 'Banana'}],
  #      'Vegetal': [{'nome': 'Cenoura'},
  #                  {'nome': 'Alface'}]
  #               }

lista = [
    {"nome": "Maçã", "categoria": "Fruta"}, # Item 1, tipo DIC
    {"nome": "Banana", "categoria": "Fruta"}, # Item 2
    {"nome": "Cenoura", "categoria": "Vegetal"}, # Item 3
    {"nome": "Alface", "categoria": "Vegetal"}, # Item 4
]


""" for item in lista:
  #print(item)
  qqnome = item['nome']
  print(qqnome) """

categorias = {}  
for item in lista:
  qqnome = item['categoria']
  if qqnome in categorias:
    categorias[qqnome].append(item)
  else:
    categorias[qqnome] = [item]
    
# saida
print(categorias)