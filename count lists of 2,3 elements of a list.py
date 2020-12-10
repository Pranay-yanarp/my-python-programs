'''
create a list form the given list, which should contaian lists of two and three adjecent elements, then
print the corresponding lists whose count is greater than 2. 

'''


def trans(x1):
	
	x2=[]
	x3=[]
	for i in range(len(x1)-1):
		x2.append([x1[i],x1[i+1]])
	for i in range(len(x1)-2):
		x2.append([x1[i],x1[i+1],x1[i+2]])
	print(x1)		
	print(x2)		
	for i in x2:
		if i not in x3:
			x3.append(i)
	
	for i in x3:
		if x2.count(i)>1 :
			print(i,"-->",x2.count(i))

x=[2,3,4,7,5,8,6,3,4,7,2,3,4]

trans(x)


