#break statement
for i in range(5):
    if i == 3:
      break
    print(i)
    
a=1
while a<=4:
    if a ==3:
        break
    print(a)
    a+=1

#continue statement
for i in range(5):
    if i == 3:
      continue
    print(i)

a=0
while a<=4:
    a+=1
    if a ==3:
        continue
    print(a)
   
#pass statement
for i in range(5):
    if i == 6:
        pass
    print(i)

a=1
while a<=4:
        pass
        a+=1
        print(a)
    
# regular expression
import re
test = "My name is Hello World"
result= re.search("is",test) 
print(result)   

# re.search, re.match,re.find all,re.sub,re.find it, re.splits
import re
t = "my name is shubham"
print(re.search("name",t))
print(re.match('my',t))
print(re.sub("shubham","Aashiq",t))
z="cat bat rat hat that"
print(re.findall("at",z))
for i in re.finditer("at",z):
    print(i.start())
s="banana,apple,grapes"
print(re.split(" ",s))

# mobile verification and email verification
import re
monile_pattern=r"^[6-9]\d{9}$"
mobile=input("Enter a mobile number: ")
if re.match(monile_pattern,mobile):
    print(mobile)
else:
    print('invalid number')

email_pattern=r"^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.%+-]+\.[a-zA-Z]{2,}$"
email=input("enter a email: ")
if re.match(email_pattern,email):
    print(email)
else:
    print("invalid email")

# recursion
def fact(n):
    if n==1 or n==0:
        return 1
    return fact(n-1)*n
print(fact(5))

def fibo(n):
    if n==0:
        return 0
    elif n<0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
print(fibo(0))

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(12,144))

def hs(n):
    if n==1:
        return 1
    return 1/n + hs(n-1)
print(hs(2))

# numpy to do all operations on matrix
import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
#sum,sub,multi,transpose,determinant,inverse
print(A+B)
print(A-B)
print(np.dot(A,B))
print(A.T)
print(np.linalg.det(A))
print(np.linalg.inv(A))

#random , math , built in module 
import random
i=print(random.randint(1,29))
import math
sq = print(math.sqrt(9))
fact= print(math.factorial(7))
pi = print(math.pi)
print(random.random())



