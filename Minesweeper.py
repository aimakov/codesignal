## Code to return matrix with amount of mines around each cell

def minesweeper(matrix):

	ans = [[0 for x in range(len(matrix[0]))] for x in range(len(matrix))]

	for x in range(len(matrix)):
		for y in range(len(matrix[0])):
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
			ans[x][y] = temp
	return ans

matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

print(test(matrix))