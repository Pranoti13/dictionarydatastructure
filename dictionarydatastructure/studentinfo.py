#Q.Write a program to accept student name and marks from the keyboard and creates a dictionary. Also display student marks by taking student name as input?
n=int(input("enter the no of students:"))
d={}
for i in range(n):
    name=input("enter students name:")
    marks=input("enter students marks:")
    d[name]=marks
while True:
    name=input("enter students name to get marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("student not found")
    else:
        print("the marks of",name,"are",marks)
    option=input("do you want to find another student marks[Yes|No]")
    if option=="No":
        break
print("thanks for using our application")'''