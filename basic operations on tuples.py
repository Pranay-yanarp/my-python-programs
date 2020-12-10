# print data type of elements of a tuple

ef=(4,"py",[1,2])
print(type(ef[0]))
print(type(ef[1]))
print(type(ef[2]))
print(ef)

# print index and corresponding element of a tuple

gh=(4,"py",[1,2])
for i in range(len(gh)):
	print(i," ",gh[i])

# print all the elements of different data types, of a tuple in a single string

gh=(4,"py",[1,2,"inlist1"],(5,6),2.45)
sti=""
for i in gh:
	if type(i) is int:
		sti=sti+str(i)
	elif type(i) is str:
		sti=sti+i
	elif type(i) is float:
		sti=sti+str(i)	
	elif type(i) is list:
		for j in i:		
			if type(j) is int:
				sti=sti+str(j)
			elif type(j) is str:
				sti=sti+j
			elif type(j) is float:
				sti=sti+str(j)		
	elif type(i) is tuple:
		for j in i:		
			if type(j) is int:
				sti=sti+str(j)
			elif type(j) is str:
				sti=sti+j
			elif type(j) is float:
				sti=sti+str(j)			
print(sti)	


# print a string in reverse

stte=input("enter a string : ")
sd=""
for i in range(len(stte)-1,-1,-1):
	sd=sd+stte[i]
print(sd)

# print non-tuple elements in a tuple using while

tup1=(4,"py",[1,2,"inlist1"],(5,6),2.45)
i=0
count=0
while(type(tup1[i])!=tuple):
 	count+=1
 	i+=1
print(count)

# remove an element from a tuple

tup1=(4,"py",[1,2,"inlist1"],(5,6),2.45)

print(tup1)
tup1=list(tup1)
tup1.remove(4)
print(tuple(tup1))

























