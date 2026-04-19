 #wap to get integer half:half in palindrome
# k = input("Enter the value :")
# if(k[:len(k)//2]) == (k[len(k)//2:][::-1]):
#     print("Palidrone Candidate")
# else: 
#     print("NOt a palidrone")

# wap to check a str is pLINDROME or not
# s = input("enter a string")
# if s==s[::-1]:
#     print('palindrome')
# else:
#     print('not a palindrome')

# wAP to print greatest and smllest from given number
# a=[10,20,30,[40,50]] 
# b=a.copy()
# print(b)
# a[0]=300
# a[3][1]=100
# print(a)
# print(b)

# a=[10,20,30,[40,50]] 
# import copy
# b=copy.deepcopy(a)
# a[0]=3000
# b[3][1]=60
# print(a)
# print(b)

# a= 1
# while a<=10:
#     print(a)
#     a+=1


# a= 10
# while a>=1:
#     print(a)
#     a-=1

# a= 2
# while a<=50:
#     print(a)
#     a+=2

# a = 1
# fact = 1
# n = int(input("Enter the value"))
# while a<=n:
#     fact=fact*a
#     a+=1
# print(fact)
    
# wap to print the product the f indivual digital in number
# n = int(input("enter the value"))
# r = 1
# while n>0:
#     digit=n%10
#     r=r*digit
#     n=n//10
# print(r)

# wap to print reverse of a number 
# n = int(input("enter the value"))
# r = 0
# while n>0:
#     digit=n%10
#     r=r*10+digit
#     n=n//10
# print(n)

# wap to extract the vowels from the given string
# s = input("Enter a name")
# i = 0
# vowels = ""
# while i < len(s):
#     if s[i] in "aeiouAEIOU":
#         vowels = vowels + s[i]
#     i += 1
# print(vowels)

# wap to elimate duplicate from list without list
# arr = [1, 1, 1, 2, 2, 3, 4, 4, 5]
# i = 0
# while i < len(arr):
#     j = i + 1
#     while j < len(arr):
#         if arr[i] == arr[j]:
#             arr.pop(j)
#         else:
#             j += 1
#     i += 1
# print(arr)

# wap to elimate duplicate from list with list
# ls= [1,2,1,3,4,5,6,7]
# l =[]
# i = 0
# while i<len(ls):
#     if ls[i] not in l:
#         l.append(ls[i])
#     i+=1
# print(l)

# wap to print a new string from the old string by extracting only capital letters and while loop , ascii values, 
# Ascii -> American Standard Code for Information Interchange
# A-> 65, a-> 97
# s=input("enter a string")
# s1=""
# i=0
# while i<len(s):
#     if 65<=ord(s[i])<=90:
#         s1+=s[i]
#     i+=1
# print(s1)
          
# wap to calculate count of the spy numbers in a list {sum=multiple}
# num = [1124, 123, 141, 22, 31, 213,64, 21]
# c = 0
# i = 0
# while i < len(num):
#     n = num[i]
#     a = n
#     s = 0
#     p = 1
#     while a > 0:
#         digit = a % 10
#         s += digit
#         p *= digit
#         a //= 10
#     if s == p:
#         c += 1
#     i += 1
# print(c)

# variable.split(character,no of splits)
# "joining value".join(variable)
#  wap to print python is a snake in nohtyp si a ekans
# s = input("enter the value")
# o = []
# a = s.split()
# for i in a:
#     o.append(i[::-1])
# print(" ".join(o))

# wap to print {str:rts}
# s=input("enter the string:")
# dict={}
# x=s.split()
# for i in x:
#     dict[i]=i[::-1]
# print(dict)    

# wap to print I AM SHUBHAM 
# s = "I AM SHUBHAM"
# for i in s.split():
#     print(i)
#     print(type(i))
    
# WAP TO 'I@anA@ditya@Sahu'
# s = 'I@anA@ditya@Sahu'
# for i in s.split('@'):
#     print(i)
    
# wap to check the evil number or not
# n = int(input("enter a number"))
# print(bin(n))
# if n<0:
#     print('enter a positive number')
# else:
#     c = bin(n).count('1')
#     if c%2==0:
#         print("evil number")
#     else:
#         print("not evil number")

# l = ['shubham','is','a','boy']
# print('@'.join(l))

#Wap to make a anagram
# s1=input("enter s1")
# s2=input("enter s2")
# if len(s1)!=len(s2):
#     print("Not anagram")
# else:
#     f1={}
#     f2={}
#     for ch in s1:
#         f1[ch]=f1.get(ch,0)+1
#     for ch in s2:
#         f2[ch]=f2.get(ch,0)+1
# if f1 == f2 :
#     print("Anagram")
# else:
#     print("Not Anagram")

# wap to check if two strings have any common ch or not
# st1=input("Enter a str1")
# st2=input("Enter a str2")
# for i in st1:
#     for j in st2:
#         if i==j:
#             print("COMMAN",i)
            
# wap input='Alphabet' output="platebah"
# s= "alphabet"
# j=""
# h=""
# i=7
# while i>=0:
#     if i>2:
#         j=j+s[i]
#     else:
#         h=h+s[i]
#     i-=1
# print(h+j)

#wap to input="Python is a good language" output="nohtyp si a doog egaugnal"
# s="Python is a good language"
# i =''
# j= ''
# for a in s:
#     if a==" ":
#         i=i+j+' '
#         j=' '
#     else:
#         j=a+j
# print(i+j)

#wap to merge to sort two arrays
# a=[1,3,7,5]
# b=[2,4,6]
# c=[]
# c=a+b
# i=0
# m=6
# while i<m:
#     j=0
#     while j<m-1:
#         if c[j]>c[j+1]:
#             f=c[j]
#             c[j]=c[j+1]
#             c[j+1]=f
#         j=j+1
#     i=i+1
# print(c)

#wap to rotate in left side if k =2 input = [1,2,3,4,5] output= [3,4,5,1,2]
# a=[1,2,3,4,5]
# k=int(input("Enter a value:"))
# n=len(a)
# for i in range(0,k,1):
#     b=a[0]
#     j=0
#     while j<n-1:
#         a[j]=a[j+1]
#         j+=1
#     a[n-1]=b
# print(a)
# #with inbuilt fxn
# ls=[1,2,3,4,5]
# i=0
# while i<k:
#     ls1=ls.pop(0)
#     ls.append(ls1)
# i+=1
# print(ls)

# wap to print *** in 5 rows
# for i in range(5):
#     for j in range(3):
#         print("*",end="")
#         i+=1
#     print()

# wap to print 
# ***** 
# *   *
# *   *
# *   *
# ***** 
for i in range(5):
    if  i==1 or i == 2 or i==3 :
        print("*   *")
    else:
        for j in range(5):
         print("*",end="")
    i+=1
    print() 
     
# wap to print 
# for i in range(5):
#         for j in range(5):
#             if i==j:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         i+=1
#         print() 
 
    

    