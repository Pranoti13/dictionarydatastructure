#find greater from three num and find greater num is even or odd and find even num is less than 20 or not
a,b,c=eval(input("enter three num:"))
if(a>b and a>c):
    greater=a
elif(b>a and b>c):
    greater=b
else:
    greater=c
print("the greatest num is=",greater)
if(greater%2==0):
    even=greater
    print("greater num is even")
if(even<20):
    print(even,"num is less than 20")
else:
    print(even,"num is not less than 20")


