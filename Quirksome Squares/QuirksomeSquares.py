from itertools import product
from math import pow

def convert_to_int(tuple):
	return int(''.join(map(str,tuple)))
	
def read_input(dir):
	input = open(dir)
	for line in input:
		yield int(line)

def quirksome_squares(input):
	output = open("o&utput.txt", 'w')
	for i in read_input(input):
		for prod in product('1234567890', repeat=i):
			half = len(prod)/2
			if pow((convert_to_int(prod[half:]) + convert_to_int(prod[:half])), 2) == convert_to_int(prod):
				for num in prod:
					output.write(str(num))
				output.write('\n')
	output.close()
		
###############################################################################

if __name__ == '__main__':
	quirksome_squares('input.txt')