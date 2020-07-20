## code to replace an element in array

def arrayReplace(inputArray, elemToReplace, substitutionElem):
	for i in range(len(inputArray)):
		if inputArray[i] == elemToReplace:
			inputArray[i] = substitutionElem
	return inputArray

inputArray = [1, 2, 1]
print(arrayReplace(inputArray,1,3))