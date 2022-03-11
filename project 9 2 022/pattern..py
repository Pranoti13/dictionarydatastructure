'''
r=range(0,3)
c=range(0,3)
for i in r:
    for j in c:
        print("*",end=" ")
    print("\n")
'''

'''r=eval(input("enter no "))
for i in range(r):
    for j in range(r):
        print("*",end=" ")
    print("\n")'''

for i in range(3):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")

