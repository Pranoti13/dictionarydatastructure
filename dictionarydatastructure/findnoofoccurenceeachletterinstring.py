#write a program to find number of occurence of ecah letter present in the given string?

word=input("enter any word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
for k,v in d.items():
        print(k,"occured",v,"times")
