#how to delete elet from dictionary
#del d[key]
#ex.
'''d={100:"durga",200:"ravi",300:"shiva"}
del d[200]
print(d)'''

#remove all entry from dictinary
#d.clear()
'''d.clear()
print(d)'''

#delete total dictionary we cannot access d
#del d
d={100:"pk",200:"rk",300:"tk"}
#print(d)
del d


#important fun on dictionary
#1.pop()
d={100:"durga",200:"ravi",300:"shiva"}
print(d.pop(100))
print(d)
#2.popitem()
d={100:"durga",200:"ravi",300:"shiva"}
print(d)
print(d.popitem())
#3.keys()
d={100:"durga",200:"ravi",300:"shiva"}
print(d.keys())
for k in d.keys():
    print(k)
#4.values()
d={100:"durga",200:"ravi",300:"shiva"}
print(d.values())
for v in d.values():
    print(v)
#5.items()
d={100:"durga",200:"ravi",300:"shiva"}
for k,v in d.items():
    print(k,"--",v)              #"= or - or : or --"

#6.copy()
d={100:"durga",200:"ravi",300:"shiva"}
d1=d.copy()
print(d1)
#7.setdefault()
d={100:"durga",200:"ravi",300:"shiva"}
print(d.setdefault(100))
print(d.setdefault(100,"pavan"))
print(d)
print(d.setdefault(400,"sachin"))
print(d)
#8.update()
#d={100:"durga",200:"ravi",300:"shiva"}
#d.update(x)                           # x is not defined ....error

#9.dictionary comprehension
squares={x:x*x for x in range(1,6)}
print(squares)
doubles={x:2*x for x in range(1,6)}
print(doubles)


