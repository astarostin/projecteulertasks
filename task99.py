import utils
import math

def main():
	print 'task 99'
	n = 1
	max_n = 0
	max_val = 0
	
	with open('data/task99.txt', 'r') as f:
		for line in f:
			nums = line.split(',')
			a = int(nums[0])
			b = int(nums[1])
			val = b * math.log(a)
			if val > max_val:
				max_val = val
				max_n = n
			n += 1
	print max_n
	
if __name__ == '__main__':
	main()