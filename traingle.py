#program to check whether the 3 values forms the sides of a triangle
i=0
source=[]
print("array values are")
for i in range(0,3):
	source.append(int(input()))
print("The values are",source)

a=source[0]
b=source[1]
c=source[2]

count=0
if(a+b>c):
	count=count+1
if(b+c>a):
	count=count+1
if(c+a>b):
	count=count+1

if(count>=2):
	print("You got a triangle")
else:
	print("It is not a triangle")
