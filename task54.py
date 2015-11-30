
HANDS = {'HIGH_CARD': 1,
		 'ONE_PAIR': 2,
		 'TWO_PAIRS': 3,
		 'THREE_OF_A_KIND': 4,
		 'STRAIGHT': 5,
		 'FLUSH': 6,
		 'FULL_HOUSE': 7,
		 'FOUR_OF_A_KIND': 8,
		 'STRAIGHT_FLUSH': 9,
		 'ROYAL_FLUSH': 10}

CARDS = {'2': 2,
		 '3': 3,
		 '4': 4,
		 '5': 5,
		 '6': 6,
		 '7': 7,
		 '8': 8,
		 '9': 9,
		 'T': 10,
		 'J': 11,
		 'Q': 12,
		 'K': 13,
		 'A': 14}


def main():
	print 'Task 54'

	first_wins = 0
	second_wins = 0
	with open('data/task54.txt', 'r') as f:
		for line in f.readlines():						
			cards = line.split()	
			hand1 = cards[:5]
			hand2 = cards[5:]			
			rating1 = get_rating(hand1)
			rating2 = get_rating(hand2)
			win = compare_ratings(rating1, rating2)
			if win == 1:
				first_wins += 1
			elif win == -1:
				second_wins += 1
	print first_wins, second_wins


def get_rating(hand):
	res = check_flush_or_straight(hand)
	if res is not None:
		return res
	res = check_counts_of_a_kind(hand)
	if res is not None:
		return res
	raise ValueError('Rating is None found for ' + str(hand))


def check_flush_or_straight(hand):
	same_suit = len(set([h[1] for h in hand])) == 1
	values = sorted([CARDS[h[0]] for h in hand], reverse=True)
	diff = 0
	for i in xrange(4):
		diff += values[i] - values[i + 1]
	if diff == 4 and not same_suit:
		res_major = 'STRAIGHT'
	elif same_suit and diff != 4:
		res_major = 'FLUSH'
	elif same_suit and diff == 4:
		res_major = 'STRAIGHT_FLUSH'
		if values[0] == CARDS['A']:
			res_major = 'ROYAL_FLUSH'
	else:
		return None
	return HANDS[res_major], values


def check_counts_of_a_kind(hand):
	values = sorted([CARDS[h[0]] for h in hand], reverse=True)
	different_cards = len(set(values))
	if different_cards == 5:
		res_major = 'HIGH_CARD'
	elif different_cards == 4:
		res_major = 'ONE_PAIR'
		quadro, triple, pair1, pair2 = count_values(values)
		values.remove(pair1)
		values.remove(pair1)
		values.insert(0, pair1)
	elif different_cards == 3:
		quadro, triple, pair1, pair2 = count_values(values)
		if triple is not None:
			res_major = 'THREE_OF_A_KIND'
			values.remove(triple)
			values.remove(triple)
			values.remove(triple)
			values.insert(0, triple)
		else:
			res_major = 'TWO_PAIRS'
			values.remove(pair1)
			values.remove(pair1)
			values.remove(pair2)
			values.remove(pair2)			
			values.insert(0, min(pair1, pair2))
			values.insert(0, max(pair1, pair2))
	elif different_cards == 2:
		quadro, triple, pair1, pair2 = count_values(values)
		if quadro is not None:
			res_major = 'FOUR_OF_A_KIND'
			values.remove(quadro)
			values.remove(quadro)
			values.remove(quadro)
			values.remove(quadro)
			values.insert(0, quadro)
		else:
			res_major = 'FULL_HOUSE'
			values = [triple, pair1]

	return HANDS[res_major], values


def count_values(values):
	res = {}
	pair1 = None
	pair2 = None
	triple = None
	quadro = None
	for v in values:
		if v not in res.keys():
			res[v] = 1
		else:
			res[v] += 1
			if res[v] == 2 and pair1 is None:
				pair1 = v
			elif res[v] == 2 and pair1 is not None:
				pair2 = v
			elif res[v] == 3 and pair1 == v:
				triple = v
				pair1 = pair2
				pair2 = None
			elif res[v] == 3 and pair2 == v:
				triple = v
				pair2 = None
			elif res[v] == 4:
				quadro = v
				triple = None

	return quadro, triple, pair1, pair2


def compare_ratings(r1, r2):
	major1 = r1[0]
	major2 = r2[0]

	if major1 > major2:
		return 1
	elif major1 < major2:
		return -1
	else:
		minor1 = r1[1]
		minor2 = r2[1]
		for i in xrange(min(len(minor1), len(minor2))):
			if minor1[i] > minor2[i]:
				return 1
			elif minor1[i] < minor2[i]:
				return -1
	return 0

if __name__ == '__main__':
	main()
