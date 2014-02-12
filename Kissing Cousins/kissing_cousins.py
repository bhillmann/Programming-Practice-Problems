from collections import defaultdict as dd

def read_input():
	input = open("input.txt")
	for line in input:
		yield line

def process_input():
	tree = dd(dict)
	instructions = []
	for line in read_input():
		if line[0] == "#":
			continue
		elif line[0] == "F":
			instructions.append(line[1:].rstrip())
		elif line[0] == "R":
			name_1 = line[1:6].strip()
			name_2 = line[6:11].strip()
			dist = line[11:]
			tree[name_1][name_2] = int(dist)
		else:
			return instructions, tree	

def search_tree(tree, name):
	visited = [name]
	check = tree[name].keys()
	while(len(check)>0):
		temp = set()
		for i in check:
			visited.append(i)
			for j in tree[i].keys():
				temp.add(j)
		check = []
		for i in temp:
			check.append(i)
	print name
	print visited
	
			
			
				

def write_output():
	input = process_input()
	instructions = input[0]
	tree = input[1]
	for instruction in instructions:
		name_1 = instruction[0:5].strip()
		name_2 = instruction[5:].strip()
		print search_tree(tree, name_1)
		
			
			
			
			
	return "hi"
###############################################################################

if __name__ == '__main__':
	write_output()