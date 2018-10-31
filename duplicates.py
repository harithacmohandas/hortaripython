i=0
a=[]
print("Enter the array values")
for i in range(0,8):
	a.append(int(input()))
print("The array values are ",a)
#checking if there are duplicates
def check():
	count=0
	for i in range(0,8):
		for j in range(i+1,8):
			if(a[i]==a[j]):
				count=count+1
			else:
				count=count
	print("there are",count,"duplicates in this array")
check()
