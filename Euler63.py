def digcnt():
	ans = 1
	for num in range(2, 10):
		i = 1
		while len(str(num**i)) <= i and i<25:
			if len(str(num**i)) == i:
				ans +=1
			i+=1
	return ans