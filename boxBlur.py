# code to mimic blurring through convolution

def boxBlur(image):
	# summation = 0
	ans = [[0 for x in range(len(image[0])-2)] for x in range(len(image)-2)]

	for i in range(1,len(image)-1):
		for j in range(1,len(image[0])-1):
			summation = 0
			temp = []
			for k in range(i-1,i+2):
				for m in range(j-1,j+2):
					summation += image[k][m]
			ans[i-1][j-1] = summation//9
	return ans

image = [[36,0,18,9], 
 		[27,54,9,0], 
 		[81,63,72,45]]

print(boxBlur(image))
