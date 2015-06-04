# encoding:utf-8

class Mer:

	def __init__(self, sequence, k, distance = 0, show = False, save_file = False, name_file = 'output_mers.txt', order_lexicographical = False):
		self.sequence = sequence
		self.k = k
		self.distance = distance
		self.show = show
		self.save_file = save_file
		self.name_file = name_file
		self.order_lexicographical = order_lexicographical

	def getMers(self):
		size_sequence = len(self.sequence)
		if not self.distance:
			list_mers = [self.sequence[i:i+self.k] 
							for i in range(size_sequence) 
								if len(self.sequence[i:i+self.k]) == self.k]
			if self.order_lexicographical:
				list_mers.sort()
		else:
			list_mers = [(self.sequence[i:i+self.k], self.sequence[i+self.k+self.distance:i+self.k+self.distance+self.k])
							for i in range(size_sequence) 
								if (len(self.sequence[i:i+self.k]) == self.k
									and len(self.sequence[i+self.k+self.distance:i+self.k+self.distance+self.k]) == self.k)]
			if self.order_lexicographical:
				list_mers.sort()
		if self.show:
			print('Showing mers...')
			for i in list_mers:
				print(i)
		if self.save_file:
			f = open(self.name_file, 'w')
			for i in list_mers:
				f.write(str(i))
				f.write('\n')
			f.close()
			print('Created file \'{0}\'.'.format(self.name_file))
		return list_mers

	def getK(self):
		return self.k

def tests():
	result1 = ['TAA', 'AAT', 'ATG', 'TGC', 'GCC', 'CCA', 'CAT', 'ATG', 
				'TGG','GGG', 'GGA', 'GAT', 'ATG', 'TGT', 'GTT']
	assert (result1 == Mer('TAATGCCATGGGATGTT', 3).getMers())
	result2 = [('TAA','GCC'), ('AAT','CCA'), ('ATG','CAT'), ('TGC','ATG'),
				('GCC','TGG'), ('CCA','GGG'), ('CAT','GGA'), ('ATG','GAT'),
				('TGG','ATG'), ('GGG','TGT'), ('GGA','GTT')]
	assert (result2 == Mer('TAATGCCATGGGATGTT', 3, distance=1).getMers())
	result3 = ['AAT', 'ATG', 'ATG', 'ATG', 'CAT', 'CCA', 'GAT', 'GCC', 'GGA', 
				'GGG', 'GTT', 'TAA', 'TGC', 'TGG', 'TGT']
	assert (result3 == Mer('TAATGCCATGGGATGTT', 3, order_lexicographical=True).getMers())
	result3 = [('AAT','CCA'), ('ATG','CAT'), ('ATG','GAT'), ('CAT','GGA'),
				('CCA','GGG'), ('GCC','TGG'), ('GGA','GTT'), ('GGG','TGT'),
				('TAA','GCC'), ('TGC','ATG'), ('TGG','ATG')]
	assert (result3 == Mer('TAATGCCATGGGATGTT', 3, distance=1, order_lexicographical=True).getMers())
	print('Success in tests!')

#tests()