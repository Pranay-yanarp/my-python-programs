# find an element in a list
L=["digital","lync","hyderabad","gachibowli","kukatpally"]
A="Lync"
flag1=0
for i in L:
	if i is A:
		flag1=flag1+1
		
if flag1>=1:
		print("present in the sequence")
else:
	print("not present in the sequence")		


# perform bitwise operations

a=45
b=65
print("bitwise and = ",a&b)
print("bitwise or = ",a|b)
print("bitwise xor = ",a^b)


# find sum of digits of a number

a3=int(input("enter a number : "))
sum1=0	
while a3>0:
	sum1=(a3%10)+sum1
	a3=a3//10
print("sum of digits = ",sum1)	

# perform relational operations

a1=15
b1=2
print("a1>b1 = ",a1>b1)
print("a1<b1 = ",a1<b1)
print("a1==b1 = ",a1==b1)
print("a1!=b1 = ",a1!=b1)
