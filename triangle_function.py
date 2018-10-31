def check(a,b,c):
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
check(a=input(),b=input(),c=input())


