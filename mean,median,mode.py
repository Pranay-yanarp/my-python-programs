''' calculate mean,median,mode of three numbers'''

in1=int(input("enter 1st number : "))
in2=int(input("enter 2nd number : "))
in3=int(input("enter 3rd number : "))
	
# calculating mean
mean=(in1+in2+in3)/3



# calculating mode
insrti=str(in1)+str(in2)+str(in3)
in1c=insrti.count(str(in1))
in2c=insrti.count(str(in2))
in3c=insrti.count(str(in3))

if in1==in2 and in1==in3:
	mode=in1
elif (in1==in2 and in1!=in3) or (in1==in3 and in1!=in2):
	mode=in1
elif in2==in3 and in2!=in1:
	mode=in2	
elif in1!=in2 and in1!=in3 and in2!=in3:
	mode="0"

# calculating median

if mode=="0":
	if (in1>in2 and in1<in3) or (in1>in3 and in1<in2):
		median=in1
	elif (in2>in1 and in2<in3) or (in2<in1 and in2>in3):
		median=in2
	else:
		median=in3
	print("mean = %f \n median = %d \n mode = no mode"%(mean,median))		
else:
	if in1==in2 and in1==in3:
		print("mean = %f \n median = %d \n mode = %d"%(mean,in1,mode))
	elif (in1==in2 and in1<in3) or (in1==in3 and in1<in2) or (in1==in2 and in1>in3) or (in1==in3 and in1>in2):
		print("mean = %f \n median = %d \n mode = %d"%(mean,in1,mode))
	elif in2==in3 and in2<in1 or in2==in3 and in2>in1:
		print("mean = %f \n median = %d \n mode = %d"%(mean,in2,mode))	
	else:
		pass	



