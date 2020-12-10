numbs=int(input("enter a starting num"))
numbd=int(input("enter a ending num"))
for i in range(numbs,numbd+1):
    if(i%2==0):
        print("%d is even"%(i))
    else:
        print("%d is odd"%(i))
