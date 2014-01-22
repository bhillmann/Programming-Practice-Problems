class Scale:
	def __init__(self, note):
		if 'b' in note:
			possible_notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
		else:
			possible_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
		progression = [2, 2, 1, 2, 2, 2]
		notes = [note]
		progress = possible_notes.index(note)
		for i in progression:
			progress = (i+progress) % 12
			notes.append(possible_notes[progress])
		self.notes = notes
	
	def do_interval(self, start, direction, interval):
		if direction == 'down':
			mult = -1
		else:
			mult = 1
		try:
			position = self.notes.index(start)
		except:
			return "%s: invalid note for this key" % start
		if interval == 'second':
			position += 1*mult
		elif interval == 'third':
			position += 2*mult
		elif interval == 'fourth':
			position += 3*mult
		elif interval == 'fifth':
			position += 4*mult
		elif interval == 'sixth':
			position += 5*mult
		elif interval == 'seventh':
			position += 6*mult
		position = position % 7
		return "%s: %s %s > %s" % (start, direction, interval, self.notes[position])

def read_input():
	input = open("input.txt")
	input = list(input)
	for i in range(len(input))[::2]:
		yield input[i].rstrip(), input[i+1].rstrip().split(';')

def write_output():
	output = open('output.txt', 'w')
	for i in read_input():
		output.write("Key in Scale %s\n" % i[0])
		scale = Scale(i[0])
		for interval in i[1]:
			interval = interval.split()
			output.write(scale.do_interval(interval[0], interval[1], interval[2]) + "\n")
		output.write("\n")
	output.close()
		
		

###############################################################################

if __name__ == '__main__':
	write_output()