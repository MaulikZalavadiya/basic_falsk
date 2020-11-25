# def fun(n,m):
#     for i in range(n):
#         for j in range( n - i - 1):
#             print(' ', end=' ')
#         for j in range( i + 1):
#             print(m+'  ', end=' ')
#         print()
# n= int(input("enter no of rows:"))
# m= input("enter type:")
# fun(n,m)
##########################################################################
n=input("enter string:")

def fun1():
 are=n.split(" ")
 print(are)
 for i in are:
     print(i[::-1])
fun1()

def fun2():
    a= n.split(" ")
    for i in range(len(a)):
        if i>0:print(end=" ")
        for j in range(len(a[i])):
            print(a[i][j*2:j*2+2][::-1],end="")
fun2()



