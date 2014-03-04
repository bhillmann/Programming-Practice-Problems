def read_input():
	input = open('input.txt')
	test_cases = int(input.readline().rstrip())
	for i in range(test_cases):
		num_boxes = int(input.readline().rstrip())
		marbles = input.readline()
		yield num_boxes, marbles
		
	
def write_output():
	output = open('output.txt')
	for test_case in read_input():
		num_destination_cells, sum_min_moves = marble_game
		output.write("%d %d\n" % (num_destination_cells, sum_min_moves))	
	
def marble_game(num_boxes, marbles):
	pass
	

###############################################################################

if __name__ == '__main__':
	read_input()