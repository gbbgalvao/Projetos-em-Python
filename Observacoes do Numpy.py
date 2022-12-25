'''
contador[::2] numeros pares da lista
contador[1::2] numeros impares da lista
para selecionar os itens de uma array com mais de uma linha faça lista[:, 1:3] 
sendo primeiro a linha, depois a coluna.

# ATRIBUTOS
array.shape retorna o numero de linhas e colunas
array.ndim retorna o numero de dimensões
array.size retorna o numero de elementos
array.T inverte o numero de linhas e colunas, linhas viram colunas

# MÉTODOS
array.tolist()
array.reshape((5, 2)) ou array.reshape((5, 2), order = 'F) modifica forma mas mantém conjunto de elementos
array.resize((3, 2), refcheck = False) altera forma e tamanho
np.column_stack((elemento1, elemento2, elemento3)) cada um vira uma coluna
np.mean(array, axis = 0) média de colunas de uma array
np.mean(array, axis = 1) média de linhas de uma array
np.std(array[linha, coluna]) calcula o desvio padrão
np.sum(array[linha, coluna]) soma elementos especificados da array

# LISTAS
len() mede o tamanho de uma lista
.append() adiciona um item a lista
.pop() remove um item da lista
.copy() copia uma lista

ARRAY EM NUMPY SUPORTA APENAS 1 TIPO DE DADO POR VEZ
EX: Somente int, somente string, etc.
'''

