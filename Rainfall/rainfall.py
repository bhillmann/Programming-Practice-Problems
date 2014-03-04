from itertools import product
from collections import *
from random import sample
import sys


def point_value(point, elevation_data):
    return elevation_data[point[0]][point[1]]


def get_neighbors(point, size_map):
    possible_neighbors = list(product([-1,0,1],[-1,0,1]))
    for possible_neighbor in possible_neighbors:
        is_point = True
        temp_point = (point[0]+possible_neighbor[0], point[1]+possible_neighbor[1])
        if temp_point == point:
            continue
        for i in xrange(2):
            if not((temp_point[i] < size_map) and (temp_point[i] >= 0)):
                is_point = False
                break
        if (is_point == True):
            yield temp_point


def is_sink(point, size_map, elevation_data):
    value = point_value(point,elevation_data)
    for possible_neighbor in get_neighbors(point, size_map):
        if point_value(possible_neighbor, elevation_data) < value:
            return False
    return True


def find_sink(point, size_map, elevation_data, all_points_visited):
    points_visited = set()
    while(True):
        if all_points_visited.has_key(point):
            point = all_points_visited[point]
            break
        points_visited.add(point)
        if is_sink(point, size_map, elevation_data):
            break
        value = point_value(point, elevation_data)
        for possible_neighbor in get_neighbors(point, size_map):
            if point_value(possible_neighbor, elevation_data) < value:
                next_point = possible_neighbor
                value = point_value(possible_neighbor, elevation_data)
        point = next_point
    for found_sink in points_visited:
        all_points_visited[found_sink] = point
    return all_points_visited[point], points_visited, all_points_visited


def main():
    file_read = open(sys.argv[1])
    size_map = int(file_read.readline().rstrip())
    elevation_data = []
    for i in xrange(size_map):
        line_array = file_read.readline().rstrip().split()
        for i in xrange(len(line_array)):
            line_array[i] = int(line_array[i])
        elevation_data.append(line_array)
    file_read.close()
    counter_sinks = Counter()
    all_points_visited = {}
    all_points_not_visited = set(product(range(size_map),range(size_map)))
    while (len(all_points_not_visited)>0):
        point = sample(all_points_not_visited, 1)[0]
        found_sink = find_sink(point, size_map, elevation_data, all_points_visited)
        all_points_not_visited = all_points_not_visited.difference(found_sink[1])
        all_points_visited = found_sink[2]
        counter_sinks[str(found_sink[0])] += len(found_sink[1])
    sorted_counter_sinks = sorted(counter_sinks.values(), reverse=True)
    file_write = open("myOutput.txt", 'w')
    result = str(sorted_counter_sinks).replace(',', '').replace('[','').replace(']','')
    file_write.write(result)
    file_write.close()

###############################################################################

if __name__ == '__main__':
    main()