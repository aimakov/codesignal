## code to check if all digits of number are even

def evenDigitsOnly(n):
	for i in str(n):
		if int(i)%2==1:
			return False
	return True