#program to print array
print("______________________________")
import collections
main,new=[],[]
freq={}
array_len=int(input("enter the length of array\n"))
print("Enter array elements\n")

#entering elements into array
for i in range(0,array_len):
    var=input()
    main.append(var)
print("The array is",main)
ctr = collections.Counter(main)
new=sorted(main,key=ctr.get,reverse=True)
print("The new array is",new)
