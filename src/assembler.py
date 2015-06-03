# encoding:utf-8

from kdmer import *
from collections import defaultdict

import sys

class GrafoDeBruijn:

	def __init__(self, kdmers, k, d):
		self.kdmers = kdmers
		self.k = int(k)
		self.d = int(d)
		self.construirGrafo()

	def construirGrafo(self):
		# Configuração do grafo:
		# lista de tuplas onde cada tupla é:
		# (vertice_origem, aresta, vertice_destino)
		# exemplo: [(vertice1, aresta1, vertice2), (vertice2, aresta2, vertice3)]
		self.grafo = []

		# dicionário contendo a lista de adjacência
		# a chave é o vértice
		# o valor é uma lista de vértices
		self.dict_lista_adj = defaultdict(list) # dicionário de listas

		# dicionário para conter os vértices para poder acessar
		# rapidamente as arestas do caminho euleriano
		self.dict_arestas = {}

		# percorre a lista de kdmers
		# cada elemento da lista de kdmers é uma tupla de 2 elementos
		for tupla in self.kdmers:
			vertice_origem = tupla[0][0:self.k-1] + tupla[1][0:self.k-1]
			aresta = tupla[0] + tupla[1]
			vertice_destino = tupla[0][1:] + tupla[1][1:]
			self.grafo.append((vertice_origem, aresta, vertice_destino))
			# adiciona um elemento da lista ao dicionário
			self.dict_lista_adj[vertice_origem].append(vertice_destino)
			# adiciona no dicionário de arestas
			self.dict_arestas[vertice_origem + vertice_destino] = aresta

		# gera a lista de adjacência
		self.gerarListaAdjacencia()

		# gera os caminhos eulerianos
		self.gerarCaminhosEulerianos()

	# retorna o o grafo (lista de tuplas)
	# cada tupla: (vertice1, aresta, vertice2)
	def getGrafo(self):
		return self.grafo

	# função que gera e grava a lista de adjacência em arquivo (DeBruijn.txt)
	def gerarListaAdjacencia(self):

		lista_adj = ""

		# percorrendo o dicionário de listas
		for vertice_chave in self.dict_lista_adj:
			lista_adj += vertice_chave + " -> "
			# obtém a lista de vértices adjacentes ao vertice_chave
			lista_vertices = self.dict_lista_adj[vertice_chave]
			# percorre a lista de vértices adjacentes
			for vertice in lista_vertices:
				lista_adj += vertice + " -> "
			lista_adj += "\n"

		# grava no arquivo
		arq = open("DeBruijn.txt", "w")
		arq.write(lista_adj)
		arq.close()

	# função que retorna o dicionário que representa a lista de adjacência
	def getListaAdjacencia(self):
		return self.dict_lista_adj

	# função que gera os caminhos eulerianos
	def gerarCaminhosEulerianos(self):

		self.existeCaminhoEuleriano = False
		
		# verifica se possui algum caminho euleriano
		# se todos os vértices tem o mesmo grau de saída e entrada, escolha qualquer um deles
		# se todos (exceto 2 vértices) tem o mesmo grau de saída e entrada, e um desses 2 vértices
		# tem o grau de saída com 1 a mais que o grau de entrada, e o outro tem grau de entrada com
		# 1 a mais que grau de saída, então escolhe o vértice que tem 1 grau de saída com 1 a mais
		# do que o grau de entrada
		# em qualquer outro caso não possui circuito ou caminho euleriano.

		# dicionário com a quantidade de graus de entrada e saída de cada vértice
		# a chave é o vértice e o valor é a quantidade
		self.graus_entrada, self.graus_saida = {}, {}
		# obtém o dicionário de listas
		dict_lista_adj = self.getListaAdjacencia()

		# inicializando os a quantidade de graus de saída e entrada dos vértices
		for vertice_chave in dict_lista_adj:
			self.graus_saida[vertice_chave], self.graus_entrada[vertice_chave] = 0, 0
			lista_vertices = dict_lista_adj[vertice_chave]
			for vertice in lista_vertices:
				self.graus_saida[vertice], self.graus_entrada[vertice] = 0, 0

		# percorre o dicionário de listas
		# a chave é o vértice e o valor é uma lista de vértices adjacentes
		for vertice_chave in dict_lista_adj:
			#  obtém todos os vértices adjacentes ao vertice_chave
			lista_vizinhos = dict_lista_adj[vertice_chave]
			# a quantidade de graus de saída do vertice_chave é o tamanho dessa lista
			self.graus_saida[vertice_chave] = len(lista_vizinhos)
			# percorre todos os vértices adjacentes ao vertice_chave
			for vizinho in lista_vizinhos:
				self.graus_entrada[vizinho] += 1

		# variáveis para verificar os graus dos vértices
		todos_tem_mesmo_grau = True
		qte_vertices_grau_diferente = 0
		vertices_grau_diferente = []

		# verifica o primeiro caso (todos os vértices tem o mesmo de entrada e saída)
		for vertice in self.graus_entrada:
			if (self.graus_entrada[vertice] != self.graus_saida[vertice]):
				todos_tem_mesmo_grau = False
				if (qte_vertices_grau_diferente > 2):
					break
				else:
					vertices_grau_diferente.append(vertice)
					qte_vertices_grau_diferente += 1

		# vértice de onde começa
		vertice_inicio = ""

		if (todos_tem_mesmo_grau == True):
			self.existeCaminhoEuleriano = True
			# escolhe qualquer um para iniciar
			if (len(graus_entrada) > 0):
				vertice_inicio = graus_entrada.keys()[0]
			else:
				vertice_inicio = graus_saida.keys()[0]
		else:
			# verifica o segundo caso (exceto 2 vértices NÃO tem o mesmo grau)
			# só execute se todos NÃO tiverem o mesmo grau e a quantidade
			# de vértices de grau diferente for igual a 2
			if (qte_vertices_grau_diferente == 2):
				# pega os vértices com grau diferente de entrada e saída
				vertice1, vertice2 = vertices_grau_diferente[0], vertices_grau_diferente[1]
				if ((self.graus_saida[vertice1] + self.graus_entrada[vertice1]) == 1) and \
						((self.graus_entrada[vertice2] + self.graus_saida[vertice2]) == 1):
						self.existeCaminhoEuleriano = True
						# escolhe o vértice com grau de saída 1 a mais que o grau de entrada
						# nesse caso é o vertice1
						if (self.graus_saida[vertice1] > self.graus_entrada[vertice1]):
							vertice_inicio = vertice1[:]
						else:
							vertice_inicio = vertice2[:]

		# a segunda parte do algoritmo só executa se tiver caminho euleriano
		if (self.existeCaminhoEuleriano == True):
			pilha, self.circuito = [], []
			vertice_corrente = vertice_inicio

			while(True):
				# condição de parada: vértice corrente NÃO possuir vizinhos e a pilha estiver vazia
				if(self.graus_saida[vertice_corrente] == 0 and len(pilha) == 0):
					break
				else:
					# verifica se o vértice NÃO possui vizinhos (grau de saída 0)
					if(self.graus_saida[vertice_corrente] == 0):
						# adiciona ao circuito
						self.circuito.append(vertice_corrente)
						# remove o último elemento da pilha e seta ele como corrente
						vertice_corrente = pilha.pop()
					else:
						# se caiu aqui, é porque o vertice_corrente possui vizinhos
						# adiciona o vértice corrente na pilha
						pilha.append(vertice_corrente)
						# seleciona qualquer vizinho e remove ele da lista de vizinhos
						vizinho = self.dict_lista_adj[vertice_corrente].pop()
						# atualiza o grau de saída do vertice_corrente
						self.graus_saida[vertice_corrente] -= 1
						# atualiza o grau de entrada do vizinho
						self.graus_entrada[vizinho] -= 1
						# seta o vizinho como o vertice corrente
						vertice_corrente = vizinho[:]

			# adiciona o vertice_inicio ao circuito
			self.circuito.append(vertice_inicio)
			# inverte a lista para obter a ordem certa
			self.circuito = self.circuito[::-1]
			
			# grava o caminho euleriano no arquivo "Eulerianos.txt"
			caminho_euleriano = vertice_inicio[:]
			tam_caminho = len(self.circuito)
			for i in range(1, tam_caminho - 1):
				caminho_euleriano += " -> " + self.circuito[i]
			caminho_euleriano += " -> " + self.circuito[tam_caminho - 1]
			arq = open("Eulerianos.txt", "w")
			arq.write(caminho_euleriano)
			arq.close()

			# chama a função para reconstruir a sequência
			self.reconstruirSequencia()


	# função que remonta a sequência através das arestas
	def reconstruirSequencia(self):

		# obtém todas as arestas
		arestas, tam_circuito = [], len(self.circuito) 
		# obtém todas as arestas para poder remontar a sequência
		for i in range(0, tam_circuito):
			if(i < tam_circuito - 1):
				chave = self.circuito[i] + self.circuito[i + 1]
				arestas.append(self.dict_arestas[chave])
		
		 # obtém o tamanho das arestas
		len_arestas = len(arestas)

		# obtém a string até primeira metade da aresta (isso só vale para a primeira)
		self.sequencia = arestas[0][0:self.k]

		# a partir da segunda, obtém somente o último caractere da primeira metade da aresta
		for i in range(1, len_arestas):
			self.sequencia += arestas[i][0:self.k][-1]

		# acessa a aresta (len_arestas - self.d - 1)
		self.sequencia += arestas[len_arestas - self.d - 1][self.k:self.k + self.d]

		# obtém toda a segunda metade da última aresta
		self.sequencia += arestas[-1][self.k:]

		# escrevendo a sequência reconstruída no arquivo
		arq = open("sequencia_reconstruida.txt", "w")
		arq.write(self.sequencia)
		arq.close()


	# retorna se existe caminho euleriano
	def existeEuleriano(self):
		return self.existeCaminhoEuleriano

	# retorna o circuito
	def getCircuito(self):
		return self.circuito

	# retorna a sequência reconstruída
	def getSequencia(self):
		return self.sequencia


# obtém a quantidade de argumentos
len_args = len(sys.argv)

if len_args != 2 and len_args != 3:
	print('\nExecute: python assembler.py <arquivo_de_entrada>\n')
else:
	if len_args == 2: # entrada normal do programa
		obj_fasta = ArquivoFasta(sys.argv[1])
		kdmer = KDMer(obj_fasta.getSequencia(), obj_fasta.getK(), obj_fasta.getD())
		grafo = GrafoDeBruijn(kdmer.getMers(), obj_fasta.getK(), obj_fasta.getD())

		# verifica se existe caminho euleriano
		if (grafo.existeEuleriano()):
			# teste para verificar se as sequências batem
			if (grafo.getSequencia() == obj_fasta.getSequencia()):
				print("Sequência reconstruída com sucesso!")
			else:
				print("Falha: foi gerada uma sequência diferente da original.") 
				print("Tamanho da sequência original: %d" % len(obj_fasta.getSequencia()))
				print("Tamanho da sequência reconstruída: %d" % len(grafo.getSequencia()))
		else:
			print("Não existe caminho euleriano!")
	else: # entrada do problema do Rosalind:
		if sys.argv[2] == 'rosalind':

		else:
			print('\nExecute: python assembler.py <arquivo_rosalind> rosalind\n')
