# wap to print 1-20 by while 
# i=1
# while i<=20:
#     print(i)
#     i=i+1
 
# for i in range(1,21):
#     print(i)

# wap to print odd 1-50
# a = 1
# while a<=50:
#     if a%2!=0:
#         print(a)
#         a+=2
        
# for a in range(1,50,2):
#     print(a)

# wap tp sum n natural numbers
# a = 1
# n= int(input("enter a natural number"))
# s=0
# while a <=n:
#     s = s+a
#     a+=1
# print(s)

# su=0
# for b in range(1,n+1):
#     su = su+b
#     b+=1
# print(su)

# wap to reverse a num
# n = int(input("enter a value"))
# r=0
# while n>0:
#     d=n%10
#     r = r*10 + d
#     n = n//10
# print(r)

nu = int(input("Enter a number: "))
re = 0
temp = n
count = 0
for i in range(1, n+1):
    if temp == 0:
        break
    temp = temp // 10
    count += 1
for i in range(count):
    di = n % 10
    re = re * 10 + di
    n = n // 10
print(rev)