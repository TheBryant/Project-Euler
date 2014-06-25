import math

def primes(n):
	lis = [True for x in range(n)]
	lis[0:1] = [False, False]
	for num in range(2, int(math.ceil(n**.5))):
		lis[2*num::num] = [False for n in range(len(lis[2*num::num]))]
	primes = []
	for index, key in enumerate(lis):
		if key:
			primes.append(index)
	return primes

def Euler50(n):
	primesList = primes(n)
	lis = [0 for x in range(n+1)]
	for i in range(len(primesList)):
		if primesList[i]*2 > n:
			break
		currentSum = primesList[i]
		length = 1
		for j in range(i+1, len(primesList)):
			currentSum += primesList[j]
			length += 1
			if currentSum > n:
				break
			lis[currentSum] = max(lis[currentSum], length)
	finalList = [(lis[prime], prime) for prime in primesList if lis[prime] > 0]
	return finalList