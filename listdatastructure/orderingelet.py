#reverse()fun
'''n=[10,20,30,40]
n.reverse()
print(n)'''

#sort()fun
#ex 1.
'''n=[20,5,15,10,0]
n.sort()
print(n)
n.reverse()
print(n)'''
#ex 2.
'''s=["Dog","Banana","Cat","Apple"]
s.sort()
print(s)
#ex 3.
n=[20,10,"A","B"]
n.sort()                 #in python 2 ...valid bt in python 3 invalid
print(n)               #type error...sort fun compulsory list should contain only homogeneous elet o.w we will get type error
'''
#To sort in reverse of default natural sorting order
'''n=[40,10,30,20]
n.sort()
print(n)
n.sort(reverse=True)
print(n)
n.sort(reverse=False)
print(n)'''

#Alising and cloning
#ex 1.
'''x=[10,20,30,40]
y=x
print(id(x))
print(id(y))'''

 #ex 2.
'''x=[10,20,30,40]
y=x
y[1]=777
print(x)'''
# To implement cloning by using slice operator and copy fun
#slice operator
x=[10,20,30,40]
y=x[:]
y[1]=777
print(y)
#copy() fun
x=[10,20,30,40]
y=x.copy()
y[1]=777
print(y)
#multi oper
'''a=[10,20,30]
b=[40,50,60]
c=a+b
print(c)
c=a+40
print(c)
c=a+[40]
print(c)'''
#
'''l1=['abc','pqr','xyz']
l2=['abc','pqr','xyz']
print(l1==l2)'''

'''x=[50,20,30]
y=[40,50,60,100,200]
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)'''

'''l=[1,2,3,[4,5,6]]
l[3].remove(4)
print(l)'''

'''l=[1,2,3,'A',5,'B']
l.sort()'''

#list comprehensation

'''s=[x*x for x in range(1,11)]
print(s)
v=[2**x for x in range(1,6)]
print(v)
m=[x for x in s if x%2==0]
print(m)'''

'''num1=[10,20,30,40]
num2=[30,40,50,60]
num3=[i for i in num1 if i not in num2]
print(num3)
#common elements present in num1 and num2
num4=[i for i in num1 if i in num2]
print(num4)'''

s="welcome"
for i in s:
    print(i,end=' ')
n=len(s)
print(n)

'''s=eval(input("enter string"))
n=s.split()
print(n)
print(len(n))'''

