# encoding:utf-8

class ArquivoFasta:

	# construtor
	def __init__(self, nome_arquivo):

		# abre o arquivo para leitura
		arq = open(nome_arquivo, "r")

		# inicializa a string vazia
		self.dados = ""

		# percorre cada linha do arquivo e concatena em "dados"
		for linha in arq:
			self.dados += linha.replace(" ", "")

		# fecha o arquivo
		arq.close()

		# obtendo a primeira linha
		primeira_linha = self.dados.split("\n", 1)[0]

		# obtendo o "k"
		pos_ini_k = primeira_linha.find("k=")
		if (pos_ini_k == -1):
			pos_ini_k = primeira_linha.find("K=")
		pos_fim_k = primeira_linha.find("d=")
		if (pos_ini_k == -1):
			pos_ini_k = primeira_linha.find("D=")
		self.k = primeira_linha[pos_ini_k + 2:pos_fim_k]

		# obtendo o "d"
		pos_ini_d = primeira_linha.find("d=")
		if (pos_ini_d == -1):
			pos_ini_d = primeira_linha.find("D=")
		self.d = primeira_linha[pos_ini_d + 2:]

		# obtendo a sequência
		self.dados = self.dados.replace("\n", "")
		self.dados = self.dados.replace(primeira_linha, "").upper()


	def getSequencia(self):
		return self.dados

	def getK(self):
		return self.k

	def getD(self):
		return self.d


# teste
#fasta = ArquivoFasta("arquivo.txt")
#print(fasta.getSequencia())
#print(fasta.getK())
#print(fasta.getD())