'''from math import *
print(sqrt(4))
print(ceil(10.1))
print(floor(10.1))
print(fabs(-10.6))
print(fabs(10.6))'''
#finding members of module by using dir()fun
#dir()=to list out all members of current module
#dir(moule name)=to list all member of specified module
'''import module1
print(dir())
print(dir(module1))'''
#the special variable__name__ variable we can identify wheather the programm executed directly or as a module
'''def f1():
    if __name__=="__main__":
        print("the code executed as a programm")
    else:
        print("the code executed as a module from some other programm")'''

#working with math module:sqrt(x),ceil(x),floor(x),log(x),sin(x),tan(x)
'''from math import *
print(sqrt(4))'''
#working with random module: use these fun while devloping game , in cryptography and to generate random num on fly for authentication
#random()fun:
'''from random import *
for i in range(10):
    print(random())'''

#randint():
#uniform():
#randrange([start],stop,[step]):
#choice()


