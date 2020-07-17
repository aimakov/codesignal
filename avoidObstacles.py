# Code for finding minimum step to avoid all obstacles

def avoidObstacles(inputArray):
	for i in range(1,max(inputArray)+2):
        if i not in inputArray:
            ans = True
            for j in range(1,max(inputArray)+1):
                if i*j in inputArray:
                    ans = False
            if ans == True:
                return i