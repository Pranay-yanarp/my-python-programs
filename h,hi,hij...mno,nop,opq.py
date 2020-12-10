n=int(input("enter a number : "))
char=input("enter a character : ")
ex=ord(char)

# for printing h,hi,hij,hijk,,,,
for i in range(n):
	for j in range(i+1):
		print(chr(ex+j),end="")
	print()	
# for printing  mno,nop,opq
print("\n\n")
for i in range(n):
	for j in range(n):
		print(chr(ex+j+i),end="")
	print()		

stmt=input("enter a stmt : ")
res=input("enter a char : ")
ind=-1
for i in stmt:
	if i == res:
		ind=stmt.index(res,ind+1)
		print(ind)