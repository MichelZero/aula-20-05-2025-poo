#
# autor: Michel
# data: 24/05/2025
#
# 3. Dicionário de Dicionários (Aninhamento):
# Problema: Você tem dados sobre estudantes, onde cada
# estudante tem um nome e uma lista de notas em diferentes 
# disciplinas.
# Organize esses dados em um dicionário onde 
# a chave é o nome do estudante e o valor é outro dicionário 
# contendo as notas por disciplina. Calcule a média de cada aluno.
# Exemplo:
dado_estudantes = [
    {"nome": "Alice", "notas": {"Matemática": 8.5, "Português": 9.0}},
    {"nome": "Davi", "notas": {"Matemática": 7.0, "História": 8.0, "Geografia": 6.5}},
]
# Saída esperada (aproximada):
# {
#     'Alice': {'Matemática': 8.5, 'Português': 9.0, 'media': 8.75},
#     'Davi': {'Matemática': 7.0, 'História': 8.0, 'Geografia': 6.5, 'media': 7.17}
# }

boletim = {}
for estudante in dado_estudantes:
  #print(nome_estudante)
  nome = estudante['nome']
  notas = estudante['notas']
  soma_notas = sum(notas.values())
  numero_disciplina = len(notas)
  media = soma_notas/numero_disciplina
  notas['media'] = media
  #print(notas)
  boletim[nome] = notas
  
  
print(boletim)


# saída
#   {
# 'Alice': {'Matemática': 8.5, 'Português': 9.0, 'media': 8.75},
#  'Davi': {'Matemática': 7.0, 'História': 8.0, 'Geografia': 6.5, 'media': 7.166666666666667}
#   } 