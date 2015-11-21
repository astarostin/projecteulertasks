def main():
	st = str(2 ** 1000)
	lst = []
	for i in st:
		lst.append(int(i))
	print sum(lst)


if __name__ == '__main__':
	main()
