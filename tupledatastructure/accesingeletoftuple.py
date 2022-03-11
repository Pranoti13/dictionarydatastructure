
#using index
'''t=(10,20,30,40,50,60)
print(t[0])
print(t[-1])
print(t[100])'''
#using slice operator
t=(10,20,30,40,50,60)
print(t[2:5])
print(t[2:100])
#sorted()
t=(40,10,30,20)
t1=sorted(t)
print(t1)
t2=tuple(t1)
print(t2)
#min() max()fun
'''t=(40,10,30,20)
print(min(t))
print(max(t))
t=(10,20,"a","b")
print(min(t))'''
#cmp()fun
'''t1=(10,20,30)
t2=(40,50,60)
t3=(10,20,30)
print(cmp(t1,t3))
print(cmp(t2,t3))'''
#tuple packing unpacking
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)
p,q,r,s=t
print("p=",p,"q",q,"r=",r,"s=",s)
#
