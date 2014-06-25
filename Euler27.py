import math

def primes(n=1000000):
	lis = [True if x > 1 else False for x in range(n)]
	for num in range(2, int(math.ceil(n**.5))):
		if lis[num]:
			lis[2*num::num] = [False for x in range(len(lis[2*num::num]))]
	return [val for val,boo in enumerate(lis) if boo]

def quadPrimes():
	prime = set(primes(100000))
	ans = []
	for a in range(-999, 1000):
		for b in range(1000):
			n=0
			while (n**2+a*n+b) in prime:
				n+=1
			else:
				if n>10:
					ans.append([n, a, b])
	return max(ans)