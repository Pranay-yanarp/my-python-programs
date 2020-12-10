# print product of elements  in a list and even numbers in it
def mult(r):
	mux=1
	for i in r:
		mux=mux*i
	print("mult result is : ",mux)
	print("even numbers : ")
	for i in r:
		if i%2==0:
			print(i)	

# reverse the string			
def strrec(sad):
	print(sad)
	mad=""
	for i in range(len(sad)-1,-1,-1):
		mad=mad+sad[i]
	print(mad)	

# factorial number
def factorial(s):
	if s==0:
		return 1
	else:
		return s*factorial(s-1)	

# dictionary with keys=1-20 and values = squares of keys
def dictr():
	dictr={i:i**2 for i in range(1,21)}
	print(dictr)

# remove duplicates and reverse sort the list
def list1(sd):
	red=[]
	print("remove duplicates and reverse sort ")
	for i in sd:
		if i not in red:
			red.append(i)
	print("removed duplicates : ",red)	
	red.sort(reverse=True)
	print("reverse sorted : ",red)	



sdfg=[12,24,35,24,88,120,155,88,120,155]
z=[2,3,4,5,6,7]
sdf="pranay"
mult(z)
strrec(sdf)
print("fac result : ",factorial(4))

dictr()
list1(sdfg)

# find numbers of rabbits and chickens given number of heads and legs

def animals(heads,legs):
	for i in range(1,heads+1):
		for j in range(1,heads+1):
			if i+j == heads:
				if i*4+j*2 == legs:
					print("number of rabbits : ",i)
					print("number of chickens : ",j)

animals(35,94)

















