# Function to check if string is IP4-formatted

def isIPv4Address(inputString):
    
    if len(inputString)<7:
    	print("lol")
        # return False
    dot_count = 0
    
    for i in inputString:
    	if i == '.':
    		dot_count+=1
    if dot_count!=3:
    	print("lol5")

    print(dot_count)
    
    temp = [x for x in inputString.split('.')]
    print(temp)
    for i in temp:
    	if not i or len(temp)>4:
    		# return False
    		print("lol2")
    	for j in i:
    		if ord(j)>57 or ord(j)<48:
    			# return False
    			print("lol3")
    for i in temp:
        if int(i)>255 or i!=str(int(i)):
            # return False
            print("lol4")
            
    # return True

inputString='123.132.123.123'
# inputString='........'
print(isIPv4Address(inputString))
