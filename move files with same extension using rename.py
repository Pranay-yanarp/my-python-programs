import os
dirc=input("enter the directory : ")
os.chdir(dirc)
print('current directory is : ',os.getcwd())
print()
exten=""
filen=''

for i in os.listdir(dirc):
	if os.path.isfile(dirc+'\\'+i):
		exten=os.path.splitext(dirc+'\\'+i)[1]
		print(i,' has file has an extension : ',exten)
		exten=exten[1:]
		filname=dirc+"\\"+exten+"s"
		print('checking if directory with name : ',filname,' exists')
		if os.path.isdir(filname):
			print('YES,   directory with name : ',filname,' exists')
			os.rename(dirc+'\\'+i,filname+'\\'+i)
			print(i,' has been moved to directory : ',filname)
		else:
			print('NO,   directory with name : ',filname,' does not exists')
			os.mkdir(filname)
			print('directory with name : ',filname,' has been created')	
			os.rename(dirc+'\\'+i,filname+'\\'+i)
			print(i,' has been moved to directory : ',filname)
		print('\n\n')		
	


















