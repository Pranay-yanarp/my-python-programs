var=int(input("enter a number"))

#increasing stars
for i in range(1,var+1):
	print("*"*i)

#other format of incresing stars(this is standard format from youtube)
for i in range(1,var+1):
	for j in range(1,i+1):
		print("*",end="")
	print()	


# #decreasing stars	
for i in range(var,0,-1):
 	print("*"*i)

#to print 1,22,333,4444....
for i in range(1,var+1):
 	print(str(i)*i)

 #to print ....55555,4444,333,22,1
for i in range(var,0,-1):
 	print(str(i)*i)	
# to print star *,***,***** .... like a triangle
x=int((var/2)-1)
print("the triangle shape")
for i in range(1,int(var/2)+1):
	print(" "*(x-i+5),end="")
	print("*"*(2*i-1))

# to print * in diamond shape
x=int((var/2)-1)
print("the diamond shape")
for i in range(1,int(var/2)):
	print(" "*(x-i+5),end="")
	print("*"*(2*i-1))

for i in range(int(var/2),0,-1):
	print(" "*(x-i+5),end="")
	print("*"*(2*i-1))




