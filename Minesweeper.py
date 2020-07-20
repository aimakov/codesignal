def test(matrix,x,y):
	temp = 0
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			try:
				if i>=0 and j>=0 and (i!=x or j!=y):
					if matrix[i][j] == True:
						temp+=1
				# else:
					# print("lol2")
			except IndexError:
				pass
	return temp		

matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

ans = [[0 for x in range(len(matrix[0]))] for x in range(len(matrix))] 

for x in range(len(matrix)):
	for y in range(len(matrix[0])):
		ans[x][y] = test(matrix,x,y)

print(ans)

