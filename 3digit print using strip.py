'''print given number, its square and cube in 3 digits using "strip concept" '''

re=int(input("enter a number :"))
re2=re * re
re3=re2*re
retd=str(1+re/1000)
retd2=str(1+re2/1000)
retd3=str(1+re3/1000)

print(retd)
print(retd2)
print(retd3)
print(retd.lstrip(" 1.")+" "+retd2.lstrip(" 1.")+" "+retd3.lstrip(" 1."))

# print(retd[2:]+" "+retd2[2:]+" "+retd3[2:]+" ")