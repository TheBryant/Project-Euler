import math

def primes(n=1000000):
	lis = [True if x > 1 else False for x in range(n)]
	for num in range(2, int(math.ceil(n**.5))):
		if lis[num]:
			lis[2*num::num] = [False for x in range(len(lis[2*num::num]))]
	return [val for val,boo in enumerate(lis) if boo]

def fourDPF():
	pri = primes(1000)
	n = 1
	while True:
		n+=1
		if helper(n, pri) and helper(n+1, pri) and helper(n+2, pri) and helper(n+3, pri):
			return n


def helper(num, prime):
	i=1
	n=0
	while prime[n]**2 < num:
		if num%prime[n] ==0:
			i+=1
			while num%prime[n] == 0:
				num = num/prime[n]
		n+=1
	return True if i == 4 else False
