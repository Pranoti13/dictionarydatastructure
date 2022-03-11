#if we want to use member of module in our programm then we should import that module
'''import module1
print(module1.x)
module1.add(20,30)'''
#module1.product(30,4)       ..........attribute error

#fun is nested then this nested fun is not importodule since it has attribute error

#renaming module at the time of import(module aliasing):
#import module1 as m1

'''import module1 as m1
print(m1.x)
m1.add(3,4)'''

#from import:we can import perticular mem of module by using from import....advantage=we can access mem directly without using module name
'''from module1 import x,add
print(x)
add(3,8)'''
#product(9,3)          ...name error since product is not import from module1 it only import x and add
#if we can import all mem of module as follows ...from modulename import *
#ex.2
'''from module1 import *
print(x)
add(56,76)'''

#member aliasing
'''from module1 import x as y,add as sum
print(y)
sum(8,4)'''

#reloading module
'''import time                # time predefined module
from imp import reload       #imp ,reload predifined module
import module1
time.sleep(30)
reload(module1)
time.sleep(30)
reload(module1)'''




