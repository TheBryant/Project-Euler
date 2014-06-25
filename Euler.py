def right_solve():
	curNum = 0
	curSol = 0
	for x in range(120, 1000):
		sol = 0
		for y in range(1, x/2):
			for z in range(y, (x/2)):
				if((y**2 + z**2) == (x-y-z)**2):
					sol+=1
				elif((y**2 + z**2) > (x-y-z)**2):
					break
		if sol>curSol:
			curNum = x
			curSol = sol
	return curNum

def tph(n):
	tNum = [x*(x+1)/2 for x in range(n)]
	pNum = [x*(3*x-1)/2 for x in range(n)]
	hNum = [x*(2*x-1) for x in range(n)]
	same = []
	for tri in tNum:
		for pen in pNum:
			if tri>pen:
				pNum = pNum[1:]
			if tri == pen:
				for hexe in hNum:
					if tri>hexe:
						hNum = hNum[1:]
					if tri == hexe:
						same.append(tri)
						break
					if tri < hexe:
						break
				if tri < pen:
					break
	return same