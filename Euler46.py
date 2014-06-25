import math

def primes(n=1000000):
	lis = [True for x in range(n)]
	lis[0:2] = False, False
	for num in range(2, int(math.ceil(n**.5))):
		if lis[num] == True:
			lis[2*num::num] = [False for x in range(len(lis[2*num::num]))]
	return [num for num,prime in enumerate(lis) if lis[num]]

def odd_composites(n=1000000):
	s = {num for num in range(9, n) if num%2 != 0}
	for prime in primes(n):
		if prime in s:
			s.remove(prime)
	return s

def goldbach(n=1000000):
	comp = odd_composites(n)
	prime = primes(n)
	for num in comp:
		for p in prime:
			if helper(num, p):
				break
			if p>num:
				return num
	print("Fail")

def helper(c, p):
	for i in range(1, 1000):
		if c == p + 2*(i**2):
			return True
		elif c < p + 2*(i**2):
			return False