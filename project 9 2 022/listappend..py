list=[]
#l=list(eval(input("enter list")))
while(1):
    print("are you want to enter no")
    ch=input("please enter y/n")
    if(ch=='y'):
       # n=eval(input("enter no"))
       #l.append(n)
        list.append(eval(input("enter no")))
    else:
        print(list)
        break

