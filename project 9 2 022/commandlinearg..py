'''s="learning python is very easy!!!"
n=len(s)
i=0
print("forward direction")
while i<n:
    print(s[i],end='')
    i+=1
print("backward dir")
i=-1
while i>=-n:
    print(s[i],end='')
    i=i-1'''

'''s=input("enter main string:")
subs=input("enter substring:")
if subs in s:
    print(subs,"is found in main string")
else:
    print(subs,"not found in main string")'''

city=input("enter your city name")
scity=city.strip()
print(scity)




