## code to find the element with lowest sum of absolute difference from other elemets

def absoluteValuesSumMinimization(a):
	temp = [0 for x in a]
	max_values = 0
	ans = max(a)

	for i in range(len(a)):
		for j in range(len(a)):
			temp[i]+=abs(a[j]-a[i])
	
	for i in range(len(temp)):
		if temp[i]==min(temp) and a[i]<ans:
			ans = a[i]


	return ans

a = [2, 4, 7]
print(absoluteValuesSumMinimization(a))