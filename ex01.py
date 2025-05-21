#
# autor: Michel
# data: 2025/05/20

# 1) 
# # Problema: Dada uma string, crie um dicionário que conte a 
# frequência de cada palavra na string. 
# Ignore diferenças entre maiúsculas e minúsculas.
# Exemplo:
# texto = "O rato roeu a roupa do rei de Roma. O rato é esperto."
# Saída esperada (aproximada): {'o': 2, 'rato': 2, 'roeu': 1, ...}
'''
# exemplo de function
def maria(joao):
  contagem = joao
  return contagem

texto = "O rato roeu a roupa do rei de Roma. O rato é esperto."
print(maria(texto))
'''

texto = "O rato roeu a roupa do rei de Roma. O rato é esperto."

texto2 = texto.lower()
palavras = texto2.split()
#print(type(palavras))
#print(palavras)
#print(len(palavras))
contagem = {}
for maria in palavras:
  # print(maria)
  if maria in contagem:
    contagem[maria] += 1
  else:
    contagem[maria] = 1
    
print(contagem)