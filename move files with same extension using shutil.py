'''
input- directory
result-  files with similar extensions in the given directory should be moved into a folder(name=file extension +'s')
		if folder is already present then move the files otherwise create a new folder

'''

import os
import shutil
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
			shutil.move(i,filname)
			print(i,' has been moved to directory : ',filname)
		else:
			print('NO,   directory with name : ',filname,' does not exists')
			os.mkdir(filname)
			print('directory with name : ',filname,' has been created')	
			shutil.move(i,filname)
			print(i,' has been moved to directory : ',filname)
		print('\n\n')		
	


















# if exten is '.py':
# 			filen=dirc+'\\pys'
# 			if os.path.isdir(filen):
# 				shutil.move(i,filen)
# 			else:
# 				os.mkdir(filen)	
# 				shutil.move(i,filen)
# 		elif exten is '.jpg':
# 			filen=dirc+'\\'+'jpgs'
# 			if os.path.isdir(filen):
# 				shutil.move(i,filen)
# 			else:
# 				os.mkdir(filen)	
# 				shutil.move(i,filen)		
# 		elif exten is '.txt':
# 			filen=dirc+'\\'+'txts'
# 			if os.path.isdir(filen):
# 				shutil.move(i,filen)
# 			else:
# 				os.mkdir(filen)			
# 				shutil.move(i,filen)