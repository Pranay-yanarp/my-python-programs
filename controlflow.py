# print numbers except multiples of  3 and 5

nt=int(input("enter a number"))
for i in range(1,nt+1):
	if i%3!=0 and i%5!=0:
		print(i)

# squares of even nembers

for i in range(nt+1):
	if i%2==0:
		print(i**2)

# prints numbers which are multiples of 7 but not 2

for i in range(1,101):
	if i%2!=0 and i%7==0:
		print(i)

# print vowels in a statment

stmt=input("enter a statment")
for i in stmt:
	if i in "aeiou":
		print(i)