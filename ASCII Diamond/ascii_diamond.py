def read_input():
    input = open("input.txt")
    return list(input)[:-1]

def ascii_diamond():
    input = read_input()
    output = open("output.txt", 'w')
    for i in xrange(len(input)):
        output.write("Case %d:\n" % (i+1))
        line = input[i].split()
        d = Diamond(line)
        for line in d.box:
            for letter in line:
                output.write("%s" % letter)
            output.write("\n")
    output.close()

class Diamond:
    def __init__(self, line):
        self.N = int(line[0])-1
        self.size = self.N*2+1
        self.row1 = int(line[1])
        self.col1 = int(line[2])
        self.row2 = int(line[3])
        self.col2 = int(line[4])
        self.box = self.generate_box()

    def generate_box(self):
        box = []
        num_rows = self.row2 - self.row1 + 1
        num_cols = self.col2 - self.col1 + 1
        for i in xrange(num_rows):
            row = ['.'] * num_cols
            m = (self.row1 + i) % self.size
            for j in xrange(num_cols):
                n = (self.col1 + j) % self.size
                dist = self.distance_from_center(m, n)
                if dist < self.N + 1:
                    row[j] = chr(dist % 26 + 97)
            box.append(row)
        return box

    def distance_from_center(self, m, n):
        return abs(m - self.N) + abs(n - self.N)














###############################################################################

if __name__ == '__main__':
    ascii_diamond()