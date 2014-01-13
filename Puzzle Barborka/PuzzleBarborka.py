class Piece:
	def __init__(self, sides, flats):
		self.sides = sides
		self.flats = flats

class Puzzle:
	def __init__(self, dimen, list_sides):
		self.dimen = dimen
		pieces = []
		for sides in list_sides:
			flats = 0
			for side in sides:
				if side == 'F':
					flats += 1
			pieces.append(Piece(sides, flats))		
		self.pieces = pieces

def read_input(dir):
	input = open(dir)
	dimen = input.readline().split()
	list_sides = []
	for line in input:
		line = line.rstrip()
		if line.split() == ['0','0']:
			return Puzzle(dimen,list_sides)
		elif line == '':
			continue
		else:
			list_sides.append(line)

def is_compatible(piece, check):
	return True

def build_graph(pieces):
	graph = {}
	for vertex in range(len(pieces)):
		graph[vertex] = [pieces[vertex], set()]
		for check in range(len(pieces)):
			if check == vertex:
				continue
			elif is_compatible(pieces[vertex], pieces[check]):
				graph[vertex][1].add(check)
	return graph
		
		

###############################################################################

if __name__ == '__main__':
	puzzle = read_input('input.txt')
	print build_graph(puzzle.pieces)