n=int(input("enter a number : "))
# to print stars first inc then dec
for i in range(1,n+1):
	if i!=n:
		print("*"*i)
	else:
		for j in range(n,0,-1):
			print("*"*j)

print()
# to print stars from right side		
for r in range(1,n+1):
	print(" "*(n-r)+"*"*r)
print()
#to print abcde	

for s in range(ord("a"),ord("a")+n):
	for f in range(ord("a"),s+1):
		print(chr(f),end="")
	print()
print()
#to print abcde from right side	
x=ord("a")+n-1
for e in range(ord("a"),ord("a")+n):
	print(" "*(x-e),end="")
	for a in range(ord("a"),e+1):	
		print(chr(a),end="")
	print()	