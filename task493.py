import math
import utils

def main():
	print 'task493'		
	
	c70_20 = utils.count_selections(70, 20)	
	res = 0
	selections = { k: utils.count_selections(10, k) for k in xrange(1, 11)}
	print selections
	for x in xrange(2, 8):
		c7_x = utils.count_selections(7, x)
		sums = generate_sums(x, 10, 20)		
		total = 0
		for s in sums:
			for k in s:
				total += selections[k]
		total *= c7_x
		print total, c70_20
		prob = float(total) / c70_20
		print prob
		res += x * prob
	# print c70_20
	#sums = generate_sums(2, 10, 20)
	print res
	

	
def generate_sums(amount, limit, total):
	res = []
	it = 1
	generate(it, amount, limit, total, [], res)
	return res
	
def generate(it, amount, limit, total, res, global_res):		
	for x in xrange(limit, 0, -1):				
		if x < total and it < amount:
			res.append(x)
			generate(it + 1, amount, limit, total - x, res[:], global_res)
			del res[-1]
		elif x == total and it == amount:
			res.append(x)			
			global_res.append(res[:])
			del res[-1]			
		
	return global_res
	
if __name__ == '__main__':
	main()