# enter elements in a list and reverse the list

list1=[]
ds=int(input("enter number of numbers to be entered"))
for i in range(ds):
	x=int(input("enter a number"))
	list1.append(x)
list1.sort(reverse=True)
print(list1[1])	

# find mode of a list of numbers

list2=[]
list3=[]
ds=int(input("enter number of numbers to be entered"))
for i in range(ds):
	x=int(input("enter a number"))
	list2.append(x)
for i in list2:
	list3.append([list2.count(i),i])
print(list3)	
list3.sort(reverse=True)
print(list3)
if list3[0]==1:
	print("there is no mode")

else:
	print("mode is : ",list3[0][1])
	i=0
	j=1
	while list3[i][0]==list3[j][0]:
		if list3[i][1]!=list3[j][1]:
			print("mode is : ",list3[j][1]) 
		i=i+1
		j=j+1

# remove duplicates in a list

list4=[2,3,4,"hyd",4,"ret","hyd"]
list5=[]
for i in list4:
	if list4.count(i)==1:
		list5.append(i)
print(list5)		

# use list comprehensions to find even elements in another list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[i for i in a if i%2==0]
print(a)
print(b)

# sum of two matrices

mat1=[]
mat2=[]
matsm=[]
sd=[]
rs=int(input("enter num of rows : "))
cs=int(input("enter num of columns : "))
print("enter matrix 1")
for i in range(rs):
	sd=[]
	for j in range(cs):
		x=int(input("enter a number : "))
		sd.append(x)
	print("")	
	mat1.append(sd)	
print("enter matrix 2")
for i in range(rs):
	sd=[]
	for j in range(cs):
		x=int(input("enter a number : "))
		sd.append(x)
	print("")	
	mat2.append(sd)	

for i in range(rs):
	sd=[]
	for j in range(cs):
		sd.append(mat1[i][j]+mat2[i][j])
	matsm.append(sd)	
print(mat1)
print(mat2)
print(matsm)

# print tables using list comprehensions
n=int(input("enter which table you want"))
mult=[i*n for i in range(1,11)]
for i in range(1,11):
	print(n,"X",i,"=",mult[i-1])
























		