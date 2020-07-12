# Function to check if string can be rearranged into palindrome

def palindromeRearranging(inputString):
	ans = {}
	for i in inputString:
		if i in ans:
			ans[i]+=1
		else:
			ans[i]=1

	center = False

	for i in ans:
		if ans[i]%2==1:
			if center == False:
				center = True
			else:
				return False
	return True

a = 'aabb'
print(palindromeRearranging(a))