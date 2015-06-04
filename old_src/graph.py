# encoding:utf-8

class GraphDirected:

	def __init__(self, list_nodes = [], list_edges= []):
		self.nodes = list_nodes[:]
		self.edges = list_edges[:]

	def addEdge(self, src, dest):
		if src not in self.nodes:
			self.nodes.append(src)
		if dest not in self.nodes:
			self.nodes.append(dest)
		self.edges.append((src, dest))

	def showConnections(self):
		print('Showing graph\'s connections...')
		for i in self.edges:
			print(i)

	# função que retorna um dicionário contendo todos os graus de entrada e saída
	# a chave do dicionário é o nó (vértice) e
	# cada valor do dicionário é uma lista de tamanho 2 onde
	# o primeiro elemento da lista é o grau de saída
	# e o segundo elemento da lista é o grau de entrada
	def getDegrees(self):
		degree_nodes = {}
		for i in self.nodes:
			degree_nodes[i] = [0,0]
		for edge in self.edges:
			src, dest = edge
			degree_nodes[src][0] += 1
			degree_nodes[dest][1] += 1
		return degree_nodes

	# um grafo é balanceado quando todos os vértices possuem grau de entrada igual ao grau de saída
	def isBalanced(self):
		degree_nodes = self.getDegrees()
		for i in degree_nodes:
			if degree_nodes[i][0] != degree_nodes[i][1]:
				return False
		return True

	# retorna todos os sucessores de um nó dada uma posição
	def getNodeSuccessors(self, pos):
		list_successors = []
		for edge in self.edges:
			src, dest = edge
			if src == self.nodes[pos]:
				list_successors.append(dest)
		return list_successors

	# retorna a posição de um determinado nó
	def getNodePos(self, node):
		size_nodes = len(self.nodes)
		for i in range(size_nodes):
			if node == self.nodes[i]:
				return i

	# verifica se um grafo é connectado
	# faz uma DFS V vezes iniciando de cada vértice.
	# se pelo menos uma DFS não visitar todos os vértices, então o grafo
	# não é conectado
	def isConnected(self):
		size_nodes = len(self.nodes)
		for i in range(size_nodes):
			# seta todos como NÃO visitados
			visited = size_nodes*[False]
			# busca em profundidade
			def dfs(pos):
				visited[pos] = True
				list_successors = self.getNodeSuccessors(pos)
				for successor in list_successors:
					pos_successor = self.getNodePos(successor)
					if not visited[pos_successor]:
						dfs(pos_successor)
			dfs(i)
			flag_connected = True
			for j in range(size_nodes):
				if not visited[j]:
					flag_connected = False
					break
			if flag_connected:
				return True
		return False

	# função que verifica se o grau de saída de um vértice é igual ao de entrada
	# parâmetros da função: 
	#	lista de nós (vértices)
	#	dicionário contendo os graus dos vértices
	def sameDegrees(self, list_nodes, dict_degrees):
		for i in list_nodes:
				if dict_degrees[i][0] != dict_degrees[i][1]:
					return False
		return True

	# em um grafo direcionado, para conter um caminho ou circuito euleriano
	# o grafo NÃO pode ter as seguintes características:
	# 1) todos os vértices tem mesmo grau de entrada quanto saída
	# 2) todos os vértices tem o mesmo grau de entrada e saída exceto 2:
	# 		um deles tem 1 grau de saída a mais do que o grau de entrda
	# 		e o outro tem 1 grau de entrada a mais do que o grau de saída
	def containsEulerPath(self):
		# obtendo os graus de entrada e saída
		degree_nodes = self.getDegrees()
		size_nodes = len(self.nodes)
		list_nodes1, list_nodes2 = [], []
		for i in range(size_nodes):
			if degree_nodes[self.nodes[i]][0] == degree_nodes[self.nodes[i]][1]:
				list_nodes2.append(self.nodes[i])
			else:
				list_nodes1.append(self.nodes[i])
		if (len(list_nodes1) == 0 and len(list_nodes2) == size_nodes):
			# verifica se ao menos um da lista possui grau de entrada diferente do de saída
			return self.sameDegrees(list_nodes2, degree_nodes)
		elif len(list_nodes2) == 0 and len(list_nodes1) == size_nodes:
			return self.sameDegrees(list_nodes1, degree_nodes)
		elif len(list_nodes1) == 2 and len(list_nodes2) == (size_nodes-2):
			# verifica se condições 2.1 e 2.2 nos vértices do list_nodes1
			out1, in1 = degree_nodes[list_nodes1[0]]
			out2, in2 = degree_nodes[list_nodes1[1]]
			if (out1 + in1 == 1) and (out2 + in2 == 1):
				return True
		elif len(list_nodes2) == 2 and len(list_nodes1) == (size_nodes-2):
			out1, in1 = degree_nodes[list_nodes2[0]]
			out2, in2 = degree_nodes[list_nodes2[1]]
			if (out1 + in1 == 1) and (out2 + in2 == 1):
				return True
		return False

	# função que retorna todos os caminhos eulerianos de um grafo direcionado
	# algoritmo:
	# 1. iniciar a pilha e o caminho (eulerian path) como vazios
	# 	1.1 se todos os vértices tem mesmo grau de entrada quanto saída, escolher qualquer um deles
	#	1.2 se todos os vértices tem o mesmo grau de entrada e saída exceto 2 deles que
	# 		um deles tem 1 grau de saída a mais do que o grau de entrda
	# 		e o outro tem 1 grau de entrada a mais do que o grau de saída,
	#		então escolha o vértice que tem 1 grau de saída a mais do que o grau de entrada
	#	1.3 se não cair nem na condição 1.1 nem na condição 1.2, então o grafo NÃO possui caminho euleriano
	# 2. Se o vértice corrente NÃO tem aresta de saída (vizinho), adicione ao circuito, remova o último
	#    vértice da pilha e seta como o nó corrente. Senão (caso de ter vizinhos), adicione o vértice
	# 	 para a pilha, pegue qualquer um de seus vizinhos, remova a aresta entre o vértice e o vizinho
	#    selecionado e seta o vizinho como vértice corrente.
	# 3. Repita o passo 2 até o vértice corrente não ter mais aresta de saída (vizinhos) e a pilha está vazia.
	# o caminho será o inverso da lista do circuito
	# explicação retirada do algoritmo: http://www.graph-magics.com/articles/euler.php
	def getEulerPaths(self):

		list_circuits = []
		if self.containsEulerPath():
			# passo 1
			degree_nodes = self.getDegrees()
			size_nodes = len(self.nodes)
			list_nodes1, list_nodes2 = [], []
			my_nodes = []
			for i in range(size_nodes):
				if degree_nodes[self.nodes[i]][0] == degree_nodes[self.nodes[i]][1]:
					list_nodes2.append(self.nodes[i])
				else:
					list_nodes1.append(self.nodes[i])
			if (len(list_nodes1) == 0 and len(list_nodes2) == size_nodes):
				my_nodes = list_nodes2[:]
			elif len(list_nodes2) == 0 and len(list_nodes1) == size_nodes:
				my_nodes = list_nodes1[:]
			elif len(list_nodes1) == 2 and len(list_nodes2) == (size_nodes-2):
				out1, in1 = degree_nodes[list_nodes1[0]]
				out2, in2 = degree_nodes[list_nodes1[1]]
				if out1 == (in1+1):
					my_nodes.append(list_nodes1[0])
				else:
					my_nodes.append(list_nodes1[1])
			elif len(list_nodes2) == 2 and len(list_nodes1) == (size_nodes-2):
				out1, in1 = degree_nodes[list_nodes2[0]]
				out2, in2 = degree_nodes[list_nodes2[1]]
				if out1 == (in1+1):
					my_nodes.append(list_nodes2[0])
				else:
					my_nodes.append(list_nodes2[1])
			for node in my_nodes:
				current_node = node
				stack, circuit = [], []
				edges_temp = self.edges[:] # faz uma cópia de todas as arestas
				while(len(self.getNodeSuccessors(self.getNodePos(current_node))) or len(stack)):
					# passo 2
					# verifica se o vértice corrente NÃO tem aresta de saída
					if not len(self.getNodeSuccessors(self.getNodePos(current_node))):
						circuit.append(current_node) # adiciona ao circuito
						current_node = stack.pop(len(stack)-1) # remove o último da pilha e seta como nó corrente
						if not len(stack):
							circuit.append(current_node)
					else:
						stack.append(current_node) # adiciona o vértice corrente para a pilha
						# pega qualquer um de seus vizinhos
						pos = self.getNodePos(current_node)
						neighboors = self.getNodeSuccessors(pos)
						neighboor_selected = neighboors[0]
						# remove a aresta entre o vértice e o vizinho selecionado
						for i in range(len(self.edges)):
							if self.edges[i][0] == current_node and self.edges[i][1] == neighboor_selected:
								self.edges.pop(i)
								break 
						# seta o vizinho como nó corrente
						current_node = neighboor_selected
				list_circuits.append(circuit[::-1])
				# retorna com as arestas originais
				self.edges = edges_temp[:]
		else:
			print("O grafo NÃO contém caminho euleriano!")

		return list_circuits

class GraphDeBruijn():

	def __init__(self, mers, k, d):
		self.mers = mers
		self.k = k
		self.d = d
		self.edges = []
		self.edges_aux = []
		self.nodes = []
		self.info_edges = {}

		for mer in self.mers:
			prefix1 = mer[0][0:self.k-1]
			prefix2 = mer[1][0:self.k-1]

			sufix1 = mer[0][1:]
			sufix2 = mer[1][1:]

			prefix = prefix1 + prefix2
			sufix = sufix1 + sufix2

			if prefix not in self.nodes:
				self.nodes.append(prefix)

			if sufix not in self.nodes:
				self.nodes.append(sufix)

			self.edges_aux.append((prefix, sufix))
			self.info_edges[(prefix, sufix)] = (mer[0], mer[1])

		def existsEdge(src, dst):
			size_edges = len(self.edges)
			for i in range(size_edges):
				src_aux, dst_aux = self.edges[i]
				if src == src_aux and dst == dst_aux:
					return True
			return False

		size_edges_aux = len(self.edges_aux)
		for i in range(size_edges_aux):
			src, dst = self.edges_aux[i]
			if not existsEdge(src, dst):
				self.edges.append((src, dst))

		graph_bruijn = GraphDirected(self.nodes, self.edges_aux)
		self.paths = graph_bruijn.getEulerPaths()

		# lista de adjacência
		self.sucessores = {}
		size_nodes = len(self.nodes)
		for i in range(size_nodes):
			self.sucessores[self.nodes[i]] = graph_bruijn.getNodeSuccessors(i)

		suffixes = ''
		# reconstrução da sequência
		if len(self.paths) == 1:
			path = self.paths[0]
			size_edges = len(self.edges)
			size_path = len(path)
			list_sequence = []
			for i in range(0, size_path - 1):
				prefix, sufix = self.info_edges[(path[i], path[i+1])]
				if (i == (size_path - d - 2)):
					suffixes += sufix[:]
				elif i > (size_path - d - 2):
					suffixes += sufix[len(sufix)-1]
				if not i:
					list_sequence.append(prefix)
				else:
					list_sequence.append(prefix[len(prefix)-1])

			# pega o que falta para completar a sequência
			if self.k >= self.d:
				list_sequence.append(self.info_edges[(path[size_path - d - 2], path[size_path - d - 1])][1][0:self.d])
				list_sequence.append(self.info_edges[(path[size_path - 2], path[size_path - 1])][1])
			else:
				list_sequence.append(suffixes)
			# pega o último sufixo
			self.sequence = ''.join(list_sequence)
		else:
			self.sequence = ''

	def getEulerPaths(self):
		return self.paths

	def getInfoEdges(self):
		return self.info_edges

	def getSequence(self):
		if not self.sequence:
			print('Sequência vazia. Mais de um caminho euleriano!')
		return self.sequence

	def getListaAjacencia(self):
		return self.sucessores

	def getNodes(self):
		return self.nodes

def tests():
	# graph1.png
	graph1 = GraphDirected()
	graph1.addEdge(0, 1)
	graph1.addEdge(1, 2)
	graph1.addEdge(2, 3)
	graph1.addEdge(3, 0)
	graph1.addEdge(2, 4)
	graph1.addEdge(4, 2)
	assert graph1.isBalanced()
	assert graph1.isConnected()
	assert graph1.containsEulerPath()
	print(graph1.getEulerPaths())

	# graph2.png
	graph2 = GraphDirected()
	graph2.addEdge(0, 1)
	graph2.addEdge(1, 2)
	graph2.addEdge(2, 3)
	assert not graph2.isBalanced()
	assert graph2.isConnected()
	assert graph2.containsEulerPath()
	#print(graph2.getEulerPaths())

	# graph3.png
	graph3 = GraphDirected()
	graph3.addEdge(4, 5)
	graph3.addEdge(4, 6)
	assert not graph3.isBalanced()
	assert graph3.isConnected()
	assert not graph3.containsEulerPath()

	print('Success in tests!')

#tests()