def read_input():
	input = open("input.txt")
	num_routes = int(input.readline())
	routes = []
	for i in range(num_routes):
		num_stops = int(input.readline())
		j = 1
		route = []
		while(j<num_stops):
			route.append(int(input.readline()))
			j += 1
		routes.append(route)
	input.close()
	return routes

def write_output():
	routes = read_input()
	output = open('output.txt', 'w')
	for route in range(len(routes)):
		stops = maximum_sum(routes[route])
		if stops[0] == stops[1]:
			output.write("Route %d has no nice parts\n" % (route+1))
		else:
			output.write("The nicest part of route %d is between stops %d and %d\n" % (route+1, stops[0], stops[1]))
	output.close()

def maximum_sum(route):
	current_sum, max_sum, max_length, begin, current_length = (0,)*5
	for i in range(len(route)):
		current_sum += route[i]
		current_length += 1
		if current_sum < 0:
			current_sum, current_length = (0,)*2
			begin = i + 2
		elif current_sum > max_sum or (current_length > max_length and current_sum == max_sum):
			max_sum = current_sum
			max_length = current_length
	return begin, begin+max_length
	
###############################################################################

if __name__ == '__main__':
	write_output()