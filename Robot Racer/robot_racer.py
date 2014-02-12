def read_input():
	input = open("input.txt")
	maze_info = input.readline().split()
	maze = []
	for i in range(int(maze_info[0])):
		maze.append(input.readline().rstrip())
	return maze, maze_info
	input.close()


def robot_racers():
	input = read_input()
	maze = input[0]
	for i in range(len(maze)):
		if 'G' in maze[i]:
			goal = [i,maze[i].index('G')]
			break
	visited = [goal]
	fringe = get_neighbors(goal, len(maze))
	winners = []
	while(len(winners)==0):
		next_fringe = []
		for point in fringe:
			if not(point in visited):
				visited.append(point)
				entry = maze[point[0]][point[1]]
				if entry == 'O':
					next_fringe.append(point)
				elif entry == 'X':
					continue
				else:
					winners.append(entry)
		fringe = []
		for point in next_fringe:
			neighbors = get_neighbors(point, len(maze))
			for possible in neighbors:
					fringe.append(possible)
	output = open('output.txt', 'w')
	for winner in winners:
		output.write(winner + ' ')
	print winners
	output.close

def get_neighbors(point, size_maze):
	neighbors = []
	if point[0] + 1 < size_maze:
		neighbors.append([point[0] + 1, point[1]])
	if point[0] - 1 >= 0:
		neighbors.append([point[0] - 1, point[1]])
	if point[1] + 1 < size_maze:
		neighbors.append([point[0], point[1] + 1])
	if point[1] - 1 >= 0:
		neighbors.append([point[0], point[1] - 1])
	return neighbors


	
		
###############################################################################

if __name__ == '__main__':
	robot_racers()