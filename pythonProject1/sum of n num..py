n=eval(input("enter number:"))
print(n)
sum=0
'''
for i in n:
    sum=sum+i           # or sum+=i
print(sum)'''

for i in (range(1,n+1)):
    sum=sum+i
print(sum)