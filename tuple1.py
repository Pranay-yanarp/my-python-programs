t1=(1,2,3,4,5)
t2=(10,20,30,40,50)
t3=[]

for i in range(len(t2)):
	t3.append(  tuple  (  [  t1[i],t2[i]  ]  )  )
print(tuple(t3))	