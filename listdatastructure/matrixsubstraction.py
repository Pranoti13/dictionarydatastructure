#matrix substraction
m1=[[8,5,7],[15,9,12],[14,17,19]]
m2=[[3,4,6],[8,9,5],[10,14,15]]
m3=[[0,0,0],[0,0,0],[0,0,0]]
print("elets by matrix 1")
for i in range(len(m1)):
    for j in range(len(m1[i])):
        print(m1[i][j],end=' ')
    print()
print("elets by matrix 2")
for i in range(len(m2)):
    for j in range(len(m2[i])):
        print(m2[i][j],end=' ')
    print()
print("sub of matrix 1 and matrix 2")
for i in range(len(m3)):
    for j in range(len(m3[i])):
        m3[i][j]=m1[i][j]-m2[i][j]
print("sub of matrix")
for i in range(len(m3)):
    for j in range(len(m3[i])):
        print(m3[i][j],end=' ')
    print()
