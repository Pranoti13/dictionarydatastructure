# module is group of fun variable and classes saved to file
# ex 1.nested fun
x=888
def add(a,b):
    print("the sum:",a+b)
    def product(a,b):
        print("the mul:",a*b)
    product(4,5)
add(5,6)
#product(4,5)
print("Hello from model1")