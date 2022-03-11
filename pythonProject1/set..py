'''s={10,30,20,40,20,10}
print(s)
s=[10,30,50,20,20]
print(s)
s={10,30,20,50,'kdn'}
s.add(60)
s.add('infotech')
s.remove(30)
'''
l=[1,2,1,3,2,1,5,7,3]
s=set(l)            #{1,2,3,5,7}
s1=list(s)
for i in s1:
    count = 0
    for j in l:
        if(i==j):
            count +=1
            print(i,"=",count)
