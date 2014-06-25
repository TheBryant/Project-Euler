def score(hand):
	values,suits = zip(*hand)
	nums = value(values)
	nums.sort()
	if suits.count(suits[0]) == 5 and straight(nums): ###Straight Flush
		if nums[4] == 14:
			return 8*(16**5)+5 #Ace low straight
		else:
			return 8*(16**5)+num[4]
	elif nums.count(nums[0]) == 4 or nums.count(nums[1]) == 4: ###Quads
		if nums.count(nums[0])==4: #poor code for better readability
			return 7*(16**5)+nums[0]*16+nums[4]
		else:
			return 7*(16**5)+nums[4]*16+nums[0]
	elif nums.count(nums[0]) == 3 and nums.count(nums[4]) == 2: ###Full House
		return 6*(16**5)+nums[0]*16+nums[4]
	elif nums.count(nums[0]) == 2 and nums.count(nums[4]) == 3:
		return 6*(16**5)+nums[4]*16+nums[0]
	elif suits.count(suits[0]) == 5: ###Flush
		return 5*(16**5) + nums[4]
	elif straight(nums): ###Straight
		return 4*(16**5) + nums[4]
	elif nums.count(nums[0]) == 3:###Trips
		return 3*(16**5) + nums[0]*(16**2)+ nums[4]*16+nums[3]
	elif nums.count(nums[1]) == 3:
		return 3*(16**5) + nums[1]*(16**2)+ nums[4]*16+nums[0]
	elif nums.count(nums[2]) == 3:
		return 3*(16**5) + nums[2]*(16**2)+ nums[1]*16+nums[0]
	elif nums.count(nums[0]) == 2 and nums.count(nums[2]) == 2: ###Two Pair
		return 2*(16**5) + nums[2]*(16**2)+ nums[0]*16+nums[4]
	elif nums.count(nums[0]) == 2 and nums.count(nums[3]) == 2:
		return 2*(16**5) + nums[3]*(16**2)+ nums[0]*16+nums[2]
	elif nums.count(nums[1]) == 2 and nums.count(nums[3]) == 2:
		return 2*(16**5) + nums[3]*(16**2)+ nums[1]*16+nums[0]
	elif nums.count(nums[0]) == 2: ###Pair
		return 1*(16**5) + nums[0]*(16**3)+ nums[4]*(16**2)+ nums[3]*(16)+ nums[2]
	elif nums.count(nums[1]) == 2: ###Pair
		return 1*(16**5) + nums[1]*(16**3)+ nums[4]*(16**2)+ nums[3]*(16)+ nums[0]
	elif nums.count(nums[2]) == 2: ###Pair
		return 1*(16**5) + nums[2]*(16**3)+ nums[4]*(16**2)+ nums[1]*(16)+ nums[0]
	elif nums.count(nums[3]) == 2: ###Pair
		return 1*(16**5) + nums[3]*(16**3)+ nums[2]*(16**2)+ nums[1]*(16)+ nums[0]
	else:
		return nums[4]*(16**4)+nums[3]*(16**3)+nums[2]*(16**2)+nums[1]*(16**1)+nums[0]

def straight(values):
	lis = values
	if lis[4]-lis[3]==1 and lis[3]-lis[2]==1 and lis[2]-lis[1]==1 and lis[1]-lis[0]==1:
		return True
	if lis[4]==14 and lis[0]==2 and lis[1]==3 and lis[2]==4 and lis[3]==5:
		return True
	return False

def value(values):
	lis = [10 if val=='T' else val for val in values]
	lis = [11 if val=='J' else val for val in lis]
	lis = [12 if val=='Q' else val for val in lis]
	lis = [13 if val=='K' else val for val in lis]
	lis = [14 if val=='A' else int(val) for val in lis]
	return lis
	