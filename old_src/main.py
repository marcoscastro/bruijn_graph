# encoding:utf-8

from graph import *
from file_module import *
from kdmer import *
import sys

# tests ...

# test with FASTA format
my_file = File('entradas/entrada_fasta', rosalind=False)
k = my_file.getK()
d =  my_file.getD()
sequencia = my_file.getSequence()

my_file.saveFile('saidas/Sequencia_Lida.txt', sequencia)
print('\nSequencia lida gravada no arquivo: Sequencia_Lida.txt\n')
nome_arquivo = 'saidas/' + 'k' + str(k) + 'd' + str(d) + 'mer.txt'
mers = Mer(sequencia, k, distance=d, order_lexicographical=True, save_file=True, name_file=nome_arquivo).getMers()

print('\nConstruindo o Grafo De Bruijn e obtendo os caminhos eulerianos...')
print('Essa tarefa pode demorar um pouco...')
graph = GraphDeBruijn(mers, k, d)

list_adj = graph.getListaAjacencia()
str_list_adj = ''
for i in list_adj:
	str_list_adj += i + ' -> '
	for j in list_adj[i]:
		str_list_adj += j + ' -> '
	str_list_adj += '\n'

my_file.saveFile('saidas/DeBruijn.txt', str_list_adj)
print('\nLista de adjacência gravada no arquivo DeBruijn.txt')

paths = graph.getEulerPaths()
size_paths = len(paths)
print('\nO grafo possui {0} caminho(s) euleriano(s)'.format(size_paths))
if size_paths > 0:
	list_path = []
	for lista in paths:
		path_str = ''
		for item in lista:
			path_str += item + ' -> '
		list_path.append(path_str)
		list_path.append('\n')
	str_list_path = ''.join(str(i) for i in list_path)
	my_file.saveFile('saidas/Eulerianos.txt', str_list_path)
	print('\nCaminhos eulerianos gravados no arquivo Eulerianos.txt')
	if size_paths == 1:
		seq_rec = graph.getSequence()
		my_file.saveFile('saidas/Sequencia_Reconstruida.txt', seq_rec)
		print('\nSequência reconstruída gravada no arquivo Sequencia_Reconstruida.txt')


# test with Rosalind problem format
my_file = File('entradas/entrada_rosalind', rosalind=True)
graph = GraphDeBruijn(my_file.getMers(), my_file.getK(), my_file.getD())
sequence = graph.getSequence()
my_file.saveFile('saidas/saida_rosalind.txt', sequence)