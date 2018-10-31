i=0
a=[]
print("enter elements into array")
for i in range(0,5):
	a.append(int(input()))
print(a)
odd,even=[],[]
for i in range(0,5):
	if(a[i]%2==1):
		odd.append(a[i])
	else:
		even.append(a[i])
print("the odd elements are",odd)
print("the odd elements are",even)
