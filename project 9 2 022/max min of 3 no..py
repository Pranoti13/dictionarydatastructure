a,b,c=eval(input("enter three no:"))
print("a is max")if(a>b and a>c) else print("c is max") if(c>b) else print("b is max")

a,b,c=eval(input("enter three no:"))
print("a is min") if(a<b and a<c) else print("c is min") if(c<b) else print("b is min")

#print("a is min")if(eval(input("enter 1st no a="))<(eval(input("enter 2nd no b="))and (eval(input("enter 1st no a="))<(eval(input("enter 3rd no c="))) else print("c is min") if((eval(input("enter 3rd no c="))<(eval(input("enter 2nd no b="))) else print("b is min")

y=eval(input("enter any year:"))
print("is leap year") if(y%4==0) else print("is not leap year")

print("is leap year") if(eval(input("enter any year:"))%4==0) else print("is not leap year")

a=eval(input("enter your age:"))
print("eligible for voting") if(a>=18) else print("not eligible for voting")

print("eligible for voting") if(eval(input("enter your age:"))>=18) else print("not eligible for voting")

n=eval(input("enter any no:"))
print("n is divisible by 7 and is divisible by 11") if(n%7==0 and n%11==0) else print("n is not divisible by 7 and 11")
