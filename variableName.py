## code to check if name is according to following rules:
# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

def variableName(name):

	if (ord(name[0])>47 and ord(name[0])<58):
		return False

	for i in range(len(name)):
		if (ord(name[i])<97 or ord(name[i])>122) and (ord(name[i])<65 or ord(name[i])>90) and name[i]!="_" and (ord(name[i])<48 or ord(name[i])>57):
			return False
	return True