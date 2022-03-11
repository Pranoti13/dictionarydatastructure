#matrix multiplication
m1=[[2,3,4],[5,6,7],[2,5,7]]
m2=[[3,4,5],[4,5,6],[4,5,7]]
m3=[[0,0,0],[0,0,0],[0,0,0]]
print("enter elets of matrix 1")
for i in range(len(m1)):
    for j in range(len(m1[i])):
        print(m1[i][j],end=' ')
    print()
print("enter elets of matrix 2")
for i in range(len(m2)):
    for j in range(len(m2[i])):
        print(m2[i][j],end=' ')
    print()
print("multiplication of matrix 1 and matrix 2")
for i in range(len(m3)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            m3[i][j]+=m1[i][k]*m2[k][j]
print("multi=")
for i in range(len(m3)):
    for j in range(len(m3[i])):
        print(m3[i][j],end=' ')
    print()
for i in range(len(m3)):
    for j in range(len(m3[i])):
        if(i==j):
            if(m3[i][j]==1):
                continue
            else:
                break
        else:
            if(i!=j):
                if(m3[i][j]==0):
                    continue
                else:
                    break
    else:
         print(" this is identity matrix")




'''
   print("check identity matrix or not")
for i in range(len(m3)):
    for j in range(len(m3[i])):
        if i==j and m3[i][j]!=1:
            result=0
            if i!=j and m3[i][j]!=0:
                result 0
            if result==1:
                print("it is identity matrix")
            else:
                print("it is not identity matrix")
'''


