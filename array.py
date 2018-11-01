a=""
list_length=int(input("Enter the length of the list\n")) 
print("Enter the values")
for i in range(0,list_length):
	var=str(input())
	a=a+var+" "
print("The list is ",a)
array=a.split()
print("The array is ",array)
		
