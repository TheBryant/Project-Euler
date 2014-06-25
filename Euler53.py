import math

def combsel():
	i = 0
	for n in range(1, 101):
		for r in range(1, n+1):
			if (math.factorial(n)/((math.factorial(r)*(math.factorial(n-r))))) > 1000000:
				i+=1
	return i