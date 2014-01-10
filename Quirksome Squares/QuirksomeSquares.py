from itertools import product
from math import pow

def convertToInt(tuple):
	return int(''.join(map(str,tuple)))
	
def readInput(dir):
	input = open(dir)
	for line in input:
		yield int(line)

def QuirksomeSquares(input):
	output = open("Output.txt", 'w')
	for i in readInput(input):
		for j in product('1234567890', repeat=i):
			half = len(j)/2
			if pow((convertToInt(j[half:]) + convertToInt(j[:half])), 2) == convertToInt(j):
				for num in j:
					output.write(str(num))
				output.write('\n')
	output.close()
		
###############################################################################

if __name__ == '__main__':
	QuirksomeSquares('Input.txt')