'''rec={}
n=int(input("enter no of students:"))
i=1
while i<=n:
    name=input("enter student name:")
    marks=input("enter % of marks of student:")
    rec[name]=marks
    i=i+1
print("name of student","\t","% of marks")
for x in rec:
    print("\t",x,"\t\t",rec[x])'''

d=dict([(100,"durga"),(200,"shiva"),(300,"ravi")])


d.setdefault(500,"uk")
print(d)
d[400]="pk"
print(d)
d1=d.copy()
print(d1)
print(d.popitem())
print(d)
print(d.get(100,"pk"))
print(d)
print(len(d))
print(d.clear())
