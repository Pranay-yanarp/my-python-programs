# print index of matched char in str
def frg(stmt,chars):
	for i in range(len(stmt)):
		if stmt[i]==chars:
			print("index is = ",i)
stmt1=input("enter a stmt")
chars1=input("enter a char")
frg(stmt1,chars1)


# mean, median,mode of 5 numbers
def mean(a,b,c,d,e):
	print("mean is = ",(a+b+c+d+e)//5)
def median(a,b,c,d,e):
	l1=[]
	l1.append(a)
	l1.append(b)
	l1.append(c)
	l1.append(d)
	l1.append(e)
	l1.sort()
	print("median is = ",l1[2])
def mode(a,b,c,d,e):
	l1=[]
	l1.append(a)
	l1.append(b)
	l1.append(c)
	l1.append(d)
	l1.append(e)
	t1=[]
	for i in l1:
		t1.append([l1.count(i),i])
	t1.sort(reverse=True)
	if t1[0][0]==1:
		print("there is no mode")

	else:
		print("mode is : ",t1[0][1])
		i=0
		j=1
		while t1[i][0]==t1[j][0]:
			if t1[i][1]!=t1[j][1]:
				print("mode is : ",t1[j][1]) 
			i=i+1
			j=j+1

a1=int(input("enter 1 num"))
a2=int(input("enter 2 num"))
a3=int(input("enter 3 num"))
a4=int(input("enter 4 num"))
a5=int(input("enter 5 num"))
mean(a1,a2,a3,a4,a5)
median(a1,a2,a3,a4,a5)
mode(a1,a2,a3,a4,a5)