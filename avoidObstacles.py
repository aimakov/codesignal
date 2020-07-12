def avoidObstacles(inputArray):
	for i in range(1,max(inputArray)+2):
		ans = True
		for j in range(1,max(inputArray)+1):
			if i*j in inputArray:
				ans = False
		if ans == True:
			return i

inputArray = [2,3]
print(avoidObstacles(inputArray))
