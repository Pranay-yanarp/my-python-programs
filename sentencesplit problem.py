'''
print the words in "Sentence" with following rules-
1. the words parallel to 'B'in "tags" should be added to a new list
2. if 'B' is adjecent to another 'B' in tags, then the words together should be added to list.

'''

def form1(sentence1,tags1):
 	sentence1=sentence1.split()
 	entities=[]
 	newstr=""
 	tags1.append('O')
 	for i in range(len(tags1)):
 		if (tags1[i] is 'B'): 
 			if tags1[i+1] is 'B':
 				newstr+= sentence1[i]+" "
 			else:
 				newstr+= sentence1[i]
 		elif newstr!="":
 			entities.append(newstr)
 			newstr=""
 	print(entities)			
 	
Sentence = "TNS is looking for a Sr software developer to join a team that is responsible for the development and maintenance of the TNSOnline and MMIS web portals. The TNS web portal is used by internal and external customers to monitor and report on transactions processed through the TNS network."
tags = ['B', 'O', 'O', 'O', 'O', 'B', 'B', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'B', 'O','O', 'B', 'O', 'B', 'B', 'B', 'O', 'B', 'B', 'B', 'O', 'O', 'O', 'B', 'B', 'B', 'B', 'O', 'B', 'O', 'B', 'O', 'B', 'B', 'O', 'O', 'B', 'B']
form1(Sentence,tags)












