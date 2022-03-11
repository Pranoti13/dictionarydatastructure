marks=eval(input("enter marks of 5 sub:"))
sum=0
for i in marks:
    sum+=i
avg=sum/5
print(avg)
if(avg>90):
    print("garde is 'O' ")
elif(avg>80):
    print("grade is 'A' ")
elif(avg>65):
    print("grade is 'B' ")
elif(avg>50):
    print("grade is 'C' ")
elif(avg>35):
    print("pass")
elif(avg<35):
    print("fail")
elif(avg<0):
    print("not defined")
else:
    print("invalid")




