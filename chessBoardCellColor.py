## code to check if two cell on chess board are the same color

def chessBoardCellColor(cell1, cell2):
	if (ord(cell1[0])+int(cell1[1]))%2==(ord(cell2[0])+int(cell2[1]))%2:
		return True
	return False