def lychrel():
	i=0
	for num in range(1, 10000):
		if not helper(num):
			i+=1
	return i


def helper(num, iter=0):
	s = str(num+int(str(num)[::-1]))
	if s == s[::-1]:
		return True
	else:
		if iter == 50:
			return False
		else:
			return helper(int(s), iter+1)