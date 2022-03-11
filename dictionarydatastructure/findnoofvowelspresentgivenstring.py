#Q. write program to find number occurence of each vowel present in given string?
word=input("enter any word:")
vowels={'a','e','i','o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
print(d)
for k,v in sorted(d.items()):
    print(k,"occured",v,"times")