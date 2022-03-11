import string
'''for i in string.ascii_uppercase:
    print(i,end=" ")
print()

for i in string.ascii_lowercase:
    print(i,end=" ")
print()

for i in string.ascii_letters:
    print(i,end=" ")
print()'''

for i in string.ascii_lowercase:
    if(not(i=='a' or i=='e' or i=='i' or i=='o' or i=='u')):
        print(i,end=" ")
print()

for i in string.ascii_uppercase:
    if(not(i=='A' or i=='E' or i=='I' or i=='O' or i=='U')):
        print(i,end=" ")
print()
