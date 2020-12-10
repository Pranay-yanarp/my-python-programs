ret=input("enter a staring char :")
n=int(input("enter a number of chars"))
ret=ord(ret)
for i in range(n):
	print(chr(ret+i) * (i+1))
