from math import pow

def read_input():
	input = open("input.txt")
	flag = 0
	number = 0
	while(flag == 0):
		number += 1
		size = int(input.readline().rstrip())
		if (size == 0):
			flag = 1
			break		
		ordering = input.readline().split()
		terminal_nodes = input.readline().rstrip()
		num_vva = int(input.readline())
		s_tree = STree(size, ordering, terminal_nodes)
		evaluations = ''
		for i in range(num_vva):
			vva = input.readline().rstrip()
			evaluations = evaluations + s_tree.doVVA(vva)
		write_output(number, s_tree, evaluations)

def write_output(number, s_tree, evaluations):
	output = open("sTreeAnswers.txt", 'a')
	output.write("S-Tree #%i:\n" % number)
	output.write("%s\n\n" % evaluations)
	output.close()	
		
	

class STree:
	def __init__(self, size, ordering, terminal_nodes):
		self.size = size
		print self.size
		translation = range(size)
		for i in range(size):
			translation[int(ordering[i].replace("x",""))-1] = size - i - 1
		self.translation = translation
		print self.translation
		self.terminal_nodes = terminal_nodes
		print self.terminal_nodes
	
	def doVVA(self, vva):
		pos = 0
		for i in range(len(vva)):
			i = int(i)
			pos += int(int(vva[i])*pow(2, self.translation[i]))
		return self.terminal_nodes[pos]

###############################################################################

if __name__ == '__main__':
	read_input()