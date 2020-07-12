# Program to test if two arrays are similar - no more than 1 change

def areSimilar(a,b):

    a_sorted=sorted(a)
    b_sorted=sorted(b)

    if len(a_sorted)!=len(b_sorted):
        return False
    else:
        for i in range(len(a_sorted)):
            if a_sorted[i]!=b_sorted[i]:
                return False
    
    temp = 0

    for i in range(len(a)):
    	if a[i]!=b[i]:
    		temp+=1
    	if temp >2:
    		return False

    return True