# find out if given number is armstrong number
an=int(input("enter a number : "))
bn=0
cn=an
while cn>0:
	zn=cn%10
	bn=(zn**3)+bn
	cn=int(cn/10)
	
if an == bn:
	print(an,"is an armstrong number")
else:
	print(an,"is not an armstrong number")	 	

# print if the number is prime

a1=int(input("enter a number : "))
flag=0
for i in range(1,a1+1):
	if a1%i==0:
		flag=flag+1
if flag>2:
	print(a1, "is not a prime")
else:
	print(a1,"is a prime")	

# fibonnoci series
num1=1
num2=0

for i in range(1,11):
	next=num1+num2
	num2=num1
	print(num1," ",end="")
	num1=next	

# print number of even,odd in a series

a2=int(input("enter a number : "))
even,odd=0,0
for i in range(1,a2+1):
	if i%2==0:
		even=even+1
	else:
		odd=odd+1	
print("number of even = ",even)
print("number of odd = ",odd)

# pattern- decreasing stars

for i in range(5,0,-1):
	print("*"*i)

# print multiples of 9

for i in range(1,91):
	if i%9==0:
		print(i," ",end="")

# print multiples of 2 or 3 between 1-50

for i in range(1,51):
	if i%2==0 or i%3==0:
		print(i," ",end="")


# print sum of digits of a number

a3=int(input("enter a number : "))
sum1=0	
while a3>0:
	sum1=(a3%10)+sum1
	a3=a3//10
print("sum of digits = ",sum1)	










































