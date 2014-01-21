def gauss_formula(num):
	return ((num)*(num+1))/2

def street_numbers():
	output = open("output.txt", 'w')
	num_ans, house_number, last_number = (0,)*3
	while(num_ans<10):
		house_number += 1
		left_sum = gauss_formula(house_number-1)*2
		last_number = house_number + 1
		right_sum = last_number
		while(left_sum>right_sum):
			right_sum = (gauss_formula(last_number) - gauss_formula(house_number))*2
			if right_sum == left_sum:
				print '{:>10} {:>10}'.format(house_number,last_number)
				num_ans+=1
				output.write('{:>10} {:>10}\n'.format(house_number,last_number))
			last_number += 1
	output.close()

###############################################################################

if __name__ == '__main__':
	street_numbers()