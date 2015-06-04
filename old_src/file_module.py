# encoding:utf-8

class File:
	# o construtor recebe o nome do arquivo que será lido e uma variável se a leitura será
	# do arquivo do desafio do rosalind (http://rosalind.info/problems/4i/)
	def __init__(self, filename, rosalind=False):
		if rosalind:
			f = open(filename, 'r')
			l = f.readlines()
			f.close()
			new_l = [i.replace('\n','') for i in l]
			
			d, k = int(new_l.pop(0).split(' ')[1]), 0

			for i in range(len(new_l[0])):
				if new_l[0][i] != '|':
					k += 1
				else:
					break
			mers = [(i[0:k], i[k+1:]) for i in new_l]

			self.mers, self.k, self.d = mers, k, d
		else:
			arq = open(filename, 'r')
			my_list = [item.replace(' ', '') for item in arq]
			if my_list[0].find('k=') != -1:
				pos_k = my_list[0].find('k=') + 2
			else:
				pos_k = my_list[0].find('K=') + 2
			if my_list[0].find('d=') != -1:
				pos_d = my_list[0].find('d=') + 2
			else:
				pos_d = my_list[0].find('D=') + 2
			self.k = int(my_list[0][pos_k:pos_d-2].replace('\n', ''))
			self.d = int(my_list[0][pos_d:].replace('\n', ''))
			self.sequence = ''
			for i in range(1, len(my_list)):
				self.sequence += my_list[i].replace('\n', '').strip().upper()
			arq.close()

	def getMers(self):
		return self.mers

	def getK(self):
		return self.k

	def getD(self):
		return self.d

	# método que grava uma string qualquer em um arquivo
	def saveFile(self, filename, str):
		f = open(filename, 'w')
		f.write(str)
		f.close()

	def getSequence(self):
		return self.sequence
	