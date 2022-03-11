#traversing the elet of list
#by using while loop
'''n=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(n):
    print(n[i])
    i=i+1'''

#by using for loop
'''n=[0,1,2,3,4,5,6,7,8,9,10]
for n1 in n:
    print(n1)'''

#even no
'''n=[0,1,2,3,4,5,6,7,8,9,10]
for n1 in n:
    if n1%2==0:
        print(n1)'''

#elets by index wise
l=["A","B","C"]
x=len(l)
for i in range(x):
    print(l[i],"is available at +ve index:",i,"and at -ve index:",i-x)


