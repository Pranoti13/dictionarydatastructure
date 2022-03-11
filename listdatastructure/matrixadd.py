n1=[[10,20,30],[40,50,60],[70,80,90]]
n2=[[10,20,30],[40,50,60],[70,80,90]]
n3=[[0,0,0],[0,0,0],[0,0,0]]
print("elet by matrix 1:")
for i in range(len(n1)):
    for j in range(len(n1[i])):
        print(n1[i][j],end=' ')
    print()
print("elet by matrix 2:")
for i in range(len(n2)):
    for j in range(len(n2[i])):
        print(n2[i][j],end=' ')
    print()
print("add of matrix:")
for i in range(len(n3)):
    for j in range(len(n3[i])):
        n3[i][j]=n1[i][j]+n2[i][j]

print("add of matrix:")
for i in range(len(n3)):
    for j in range(len(n3[i])):
        print(n3[i][j],end=' ')
    print()

