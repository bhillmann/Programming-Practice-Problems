def build_source(source):
	source_dict = {}
	for string in source:
		source_dict[string] = []
		prefix = ''
		for char in string:
			prefix = prefix + char.lower()
			source_dict[string].append(prefix)
	return source_dict
	
def build_prefix(prefix):
	prefix_list = set()
	for string in prefix:
		prefix_list.add(string.lower())
	return prefix_list

def merged_list(source, prefix):
	source_dict = build_source(source)
	prefix_set = build_prefix(prefix)
	hit_prefix_set = set()
	merged_set = set()
	for word in source_dict.keys():
		temp_prefixes = source_dict[word]
		for temp_prefix in temp_prefixes:
			if temp_prefix in prefix_set:
				hit_prefix_set.add(temp_prefix)
				merged_set.add(word)
				break
	missed_prefix_set = prefix_set.difference(hit_prefix_set)
	return sorted(list(merged_set.union(missed_prefix_set)))
						
	
###############################################################################

if __name__ == '__main__':
	source = ['hello', 'howdy', 'jungle', 'cat', 'dog', 'funny', 'chair', 'lotion', 'noodle']
	prefix = ['hi', 'he', 'ha', 'ho', 'pre', 're', 'un', 'in', 'no', 'im', 'ju', 'do']
	print merged_list(source, prefix)