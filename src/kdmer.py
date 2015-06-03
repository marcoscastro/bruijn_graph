# encoding:utf-8

from fasta import *

class KDMer:

	def __init__(self, sequencia, K, D):

		self.lista = []
		k, d = int(K), int(D)

		len_sequencia = len(sequencia)
		for i in range(len_sequencia):
			elem1, elem2 = sequencia[i:i+k], sequencia[i+k+d:i+2*k+d]
			if (len(elem1) < k or len(elem2) < k):
				break
			self.lista.append((elem1, elem2))

		# ordem lexicográfica
		self.lista.sort()

		# escrevedo os pares no arquivo
		arq = open("kdmers.txt", "w")
		for par in self.lista:
			arq.write(par[0] + " | " + par[1] + "\n")
		arq.close()

	def getMers(self):
		return self.lista


# teste
#obj_fasta = ArquivoFasta("arquivo.txt")
#kdmer = KDMer(obj_fasta.getSequencia(), obj_fasta.getK(), obj_fasta.getD())