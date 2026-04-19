#to create and print a list the value are squares of numbers in1 to 30 with user defined fxn
# def f():
#     r = [i**2 for i in range(1,31)]
# print(r)

# n = int(input("Enter number of rows: "))
# for i in range(n):
#     num = 1
#     for j in range(n - i - 1):
#         print(" ", end="")

#     for j in range(i + 1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)

#     print()
    # wap to detect numbers of local variables in a fxn
def demo():
    x = 5
    y = 10
    z = 15
    name = "Python"
    print("Local variables:", locals())
    print("Count:", len(locals()))

demo()    