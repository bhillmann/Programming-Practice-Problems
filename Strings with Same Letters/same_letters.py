def read_input():
	input = open("input.txt")
	return list(input)[:-2]

def same_letters():
	input = read_input()
	output = open("output.txt", 'w')
	for i in range(len(input)/2):
		output.write("Case %d: " % (i+1))
		first = input[i*2]
		second = input[i*2+1]
		if sorted(first) == sorted(second):
			output.write("same\n")
		else:
			output.write("different\n")
	output.close()

###############################################################################

if __name__ == '__main__':
	same_letters()