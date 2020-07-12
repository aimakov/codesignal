# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.


example = "(sabe)(exam(bbas)(se(sb)))"
# ebasbsebsbasmaxe

a = list(example)

start = 0
end = 0
found = False
temp = 0


count = 0
for i in range(len(a)):
	if a[i] == "(":
		count += 1

for i in range(count):
	for i in range(len(a)):
		if a[i] == ")" and found == False:
			end = i
			found = True
		for i in range(end):
			if a[i] == "(":
				start = i

	middle = (end-start-1)//2

	for i in range(middle):
		temp = a[start+i+1]
		a[start+i+1] = a[end-i-1]
		a[end-i-1] = temp

	del a[start]
	del a[end-1]
	found = False

# print a
answer = ''.join(a)
print answer