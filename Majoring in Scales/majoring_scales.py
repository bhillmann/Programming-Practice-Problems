class Scale:
	def __init__(self, scale):
		if 'b' in scale:
			notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
		else:
			notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
		self.scale = scale
		self.tone = 2
		self.semitone = 1
		self.scale_progression = [self.scale, self.tone, self.tone, self.semitone,
								  self.tone, self.tone, self.tone, self.semitone]
		
###############################################################################

if __name__ == '__main__':
	print ("hellO world")
		