# print odd indexed characters of a string

stmt="pythonisbestforbeginners"
for i in range(len(stmt)):
	if i%2!=0:
		print(stmt[i])


# print a string in reverse

stmt1=input("enter a statment")
for i in range(len(stmt1),-1,-1):
	print(stmt1[i])

# use string.replace() 

stmt2=input("enter a statment")	
print(stmt2.replace(stmt2[2],"@"))

# use string.replace(), multiple times

stmt3=input("enter a statment :")	
char1=input("enter a char to be replaced :")
char2=input("enter a new char :")
ne=int(input("enter a num times to replace :"))
print(stmt3.replace(char1,char2,ne))

# print in successions of 3

stmt4=input("enter a statment :")	
for i in range(2,len(stmt4),3):
	print(stmt4[i])

# swap 2 numbers without using extra variables 

a=int(input("enter a 1st number"))
b=int(input("enter a 2nd number"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)



