def hex():
	nums = {}
	ans = []
	i=0
	while True:
		i+=1
		nums[i*(2*i-1)] = 1
		if (i*(3*i-1)/2) in nums:
			nums[i*(3*i-1)/2] += 1
		if (i*(i+1)/2) in nums:
			if nums[i*(i+1)/2] == 2:
				ans.append([i, i*(i+1)/2])
		if len(ans) > 2:
			break
	return ans
