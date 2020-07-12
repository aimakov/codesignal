# Program to calculate amount of iterations to make array strictly increasing

def arrayChange(inputArray):
	ans = 0
	for i in range(1,len(inputArray)):
		while inputArray[i]<=inputArray[i-1]:
			inputArray[i]+=1
			ans+=1
	return ans


inputArray = [1,1,1]
print(arrayChange(inputArray))

