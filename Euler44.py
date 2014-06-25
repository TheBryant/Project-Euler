def pent(): #learning generators
	n=1
	while True:
		yield n*(3*n-1)/2
		n += 1

def pennum(n=1000):
	lis = [x*(3*x-1)/2 for x in range(1, n)]
	s = {num for num in lis}
	ans = []
	for i in range(n/2):
		for j in range(i, n/2):
			if (lis[i] + lis[j]) in s and (lis[j] - lis[i]) in s:
				ans.append([lis[j], lis[i]])
	return ans