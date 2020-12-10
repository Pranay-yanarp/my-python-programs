import random
import os

def checkuser(uname):
	f1=open('D:\\thy.txt','r')
	l1=[]
	befname=''
	flag1=0
	for i in f1.readlines():

		l1=i.split(' - ')
		
		befname=l1[0]
		if uname in befname:
			print('user already exists')
			flag1=1
			break
	f1.close()	
	if flag1==1:
		return 1
	else:
		return 0	
				

def genchar(n):
	genchare=''
	for i in range(n):
		z=random.randint(65,122)
		while z>90 and z<97:
			z=random.randint(65,122)
		genchare+=chr(z)
	return genchare

def gennums(n):
	gennumse=''
	for i in range(n):
		gennumse+=str(random.randint(0,9))
	return gennumse	
	
def writefile(name,z):
	password=''
	nampas=''
	for i in range(2):
		password+=genchar(z)
		password+=gennums(z)
	f1=open('D:\\thy.txt','a')
	nampas=name+" - "+password+'\n'
	print(nampas)
	f1.write(nampas)
	f1.close()

def checkfile():
	if not (os.path.isfile('D:\\thy.txt')):
		f1=open('D:\\thy.txt','w')


flag=0
name=input("enter a name : ")
checkfile()
flag=checkuser(name)

if flag!=1:		
	pattern=int(input("enter the pattern number : "))
	writefile(name,pattern)
else:
	print("try with different name")
	