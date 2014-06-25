def pandigital(num):
	array = [False for x in range(10)]
	for digit in str(num):
		if digit == '0':
			return False
		if array[int(digit)]:
			return False
		else:
			array[int(digit)] = True
	return True