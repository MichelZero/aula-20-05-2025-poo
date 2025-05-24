
lista = [
    {"nome": "Maçã", "categoria": "Fruta"}, # Item 1, tipo DIC
    {"nome": "Banana", "categoria": "Fruta"}, # Item 2
    {"nome": "Cenoura", "categoria": "Vegetal"}, # Item 3
    {"nome": "Alface", "categoria": "Vegetal"}, # Item 4
]

for item in lista:  # percorre a lista de dicionários, item é o nome da variável que vai receber cada dicionário
  #print(item) # imprime o dicionário
  qqnome = item['nome'] # acessa o valor da chave 'categoria' do dicionário 
  print(qqnome)