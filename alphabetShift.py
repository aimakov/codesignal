## code for shifting alphabet by 1 letter

def alphabeticShift(inputString):
	ans = ''
	for i in inputString:
		if ord(i) == 122:
			ans += 'a'
		else:
			ans += chr(ord(i)+1)
	return ans

inputString = "crazy"
print(alphabeticShift(inputString))