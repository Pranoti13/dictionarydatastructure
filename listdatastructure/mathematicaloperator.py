#concatenation operator
#ex 1.
a=[10,20,30]
b=[40,50,60]
c=a+b
print(c)
#repetation operator
#ex 1.
x=[10,20,30]
y=x*3
print(y)
#comparing list 1. comparision oper(==,!=)
x=["Dog","Cat","Rat"]
y=["Dog","Cat","Rat"]
z=["DOG","CAT","RAT"]
print(x==z)
print(x!=z)
#2.relational ope(<,<=,>,>=)
x=["Dog","Cat","Rat"]
y=["Rat","Cat","Dog"]
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
#membership oper(in,not in)
n=[10,20,30,40]
print(10 in n)
print(10 not in n)
print(50 in n)
print(50 not in n)
#clear() fun
n=[10,20,30,40]
print(n)
n.clear()
print(n)
#nested lists
n=[10,20,[30,40]]
print(n)
print(n[0])
print(n[2])
print(n[2][0])
print(n[2][1])
#nested list as matrix
n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("elet by row wise:")
for r in n:
    print(r)
print("elet by matrix style:")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()
#list comprehension
#ex 1.
s=[x*x for x in range(1,11)]
print(s)
v=[2**x for x in range(1,6)]
print(v)
m=[x for x in s if x%2==0]
print(m)
#ex.2
words=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
l=[w[0] for w in words]
print(l)
#ex 3.
num1=[10,20,30,40]
num2=[30,40,50,60]
num3=[i for i in num1 if i not in num2]
print(num3)
print("common elets present in num1 and num2:")
num4=[i for i in num1 if i in num2]
print(num4)
#ex 4.
words="the quick brown fox jumps over the lazy dog".split()
print(words)
#or
'''l=words.split()
print(l)'''
l=[[w.upper(),len(w)] for w in words]
print(l)
'''l1=words.upper()
print(l1)'''

#To display unique vowels present in the given word
vowels=['a','e','i','o','u']
word=input("enter the word to search for vowels:")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print("the num of diff vowels present in",word,"is",len(found))



