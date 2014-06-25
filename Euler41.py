import math

def primes(n):
	lis=[True for x in range(n)]
	lis[0:2] = [False, False]
	for num in range(2, int(math.ceil(n**.5))):
		if lis[num]:
			lis[num*2::num] = [False for x in range(len(lis[num*2::num]))]
	primes = [key for key,val in enumerate(lis) if val]
	return primes

def pandigital(num):
	array = [False for x in range(10)]
	for digit in str(num):
		if int(digit) > len(str(num)):
			return False
		if array[int(digit)]:
			return False
		else:
			array[int(digit)] = True
	return True

def Euler41(n):
	primesList = primes(n)
	print('primes done')
	lis=[prime for prime in primesList if pandigital(prime)]
	return lis		
