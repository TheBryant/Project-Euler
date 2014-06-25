from decimal import *
import re
getcontext().prec = 10000

def recicycle():
	ans = []
	for num in range(1, 10):
		s = str(Decimal(1)/Decimal(num))
		if len(s) > 200:
			for n in range(1,50):
				match = re.findall('(\d{{{}}})'.format(n), s)
				if len(match) > 5:
					ans.append([num, n, match[2]])
					#ans.append(num)
	return ans
	#REGULAR EXPRESSIONS HAVE FAILED ME

def reci2():
	ans = []
	for num in range(1, 1000):
		s = str(Decimal(1)/Decimal(num))
		if len(s) > 200:
			for n in range(1,2000):
				if s[2:2+n] == s[2+n:2+n*2] == s[2+n*2:2+n*3]:
					ans.append([n, num])
					break
	return ans
