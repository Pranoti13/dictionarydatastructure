list=[121,211,231,321,433,342,555,659]
i=0
while(i<len(list)):
    rev = 0
    pal = list[i]
    while pal!=0:
        rem=pal%10
        rev=rev*10+rem
        pal=pal//10
  #  print(rev)
    if rev==list[i]:
        print("given no are palindrome",list[i])
    else:
        print("not palindrome",list[i])
    i=i+1

