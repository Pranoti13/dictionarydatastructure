#1.to get inf about list
#len()
'''n=[10,20,30,40]
print(len(n))'''

#count()
'''n=[1,2,2,2,2,3,3]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))'''

#index()fun
'''n=[1,2,2,2,2,3,3]
print(n.index(1))
print(n.index(2))
print(n.index(3))
print(n.index(4))'''

#2.manipulating elets of list
#append()fun
'''list=[]
list.append("A")
list.append("B")
list.append("C")
print(list)'''

'''list=[]
for i in range(101):
    if i%10==0:
        list.append(i)
print(list)'''

#insert()fun
'''n=[1,2,3,4,5]
n.insert(1,777)
n.insert(10,188)
n.insert(-10,999)
print(n)'''

#extend()fun
'''order=["chicken","mutton","fish"]
order.extend("mushroom")
print(order)
order.extend(["mushroom"])
print(order)'''

#remove()fun
n=[10,20,10,30]
n.remove(10)
print(n)

#pop()fun
#ex 1.
n=[10,20,30,40]
print(n.pop())
print(n.pop())
print(n)
#ex 2.
n=[10,20,30,40,50,60]
print(n.pop())
print(n.pop(1))
print(n.pop(10))






