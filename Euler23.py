def abund():
	val=[]
	for num in range(10, 28123):
		if sum(properDivisors(num)) > num:
			val.append(num)
	return val


def properDivisors(n):
	div=[1]
	for i in range(2, (n/2)+1):
		if n%i==0 and not i in div:
			div.append(i)
			if not n/i in div:
				div.append(n/i)
	return div

def Euler23():
	val = abund()
	print("abund out")
	nums = [True for x in range(28123+1)]
	for index,i in enumerate(val):
		for j in val[index::]:
			if i+j > 28123:
				break;
			else:
				nums[i+j] = False
	return sum(map(lambda (x,y): x if y else 0, enumerate(nums)))
