# conjunto.discard ou conjunto.remove retira um item do conjunto, conjunto.add adiciona

# conjunto = {1, 2, 3, 4, 5}
# conjunto.add(6)
# conjunto.discard(2)
# print(conjunto)

# conjunto_uniao ( une e não repete mesmos itens do conjunto), conjunto.intersection ira repetir oque foi retirado
# conjunto.difference ira imprimir a diferença dos conjuntos, conjunto.symmetric.difference(simetria e diferença)
conjunto1 = {10, 9, 8, 7}
conjunto2 = {7, 6, 5, 4}
conjunto_uniao = conjunto1.union(conjunto2)
print(conjunto_uniao)
# conjunto.issubset = imprime se verdadeiro ou falso caracteristicas de um conjunto com outro
# conjunto.issuperset = ao contrario do issubset mostra um conjunto que não se enquadra 100% a outra

# convertendo uma lista para conjunto,vise versa e retirando duplicidade

lista = ['cachorro', "gato", 'papagaio', 'papagaio', 'burro']
print(lista)
conjunto_animais = set (lista)
print(conjunto_animais)
lista_animais = list (conjunto_animais)
print(lista_animais)


