# grade the marks using conditional statments
marks=int(input("enter marks"))
if marks>=50 and marks<60:
	print("grade = E")
elif marks>=60 and marks<70:
	print("grade = D")
elif marks>=70 and marks<80:
	print("grade = C")
elif marks>=80 and marks<90:
	print("grade = B")
elif marks>=90 and marks<=100:
	print("grade = A ")				
else:
	print("grade = fail")

# find a given a year is a leap year or not using conditional statments

year=int(input("enter a year"))
if year%400==0:
	print("its a leap year")
elif year%100==0:
	print("its not a leap year")
elif year%4==0:
	print("its a leap year")
else:
	print("its not a leap year")


# find odd or even using conditional statments 

nt=int(input("enter a number"))
if nt%2==0:
	print("its even number")
else:
	print("its odd number")

# find greatest of 3 numbers using conditional statments

n1=int(input("enter a 1st number"))
n2=int(input("enter a 2nd number"))
n3=int(input("enter a 3rd number"))
if n1>n2 and n1>n3:
	print("%d is greatest"%(n1))
elif n2>n3:
	print("%d is greatest"%(n2))
else:
	print("%d is greatest"%(n3))		































