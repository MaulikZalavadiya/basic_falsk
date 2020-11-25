# def fun(*ls):
#     print(ls)
#
#     if n==2:
#      ls1.extend(ls2)
#      ls1.sort()
#      print(ls1)
#      print("max value", max(ls1))
#      print("min value", min(ls1))
#
#     elif n==3:
#         ls1.extend(ls2)
#         ls1.extend(ls3)
#         ls1.sort()
#         print(ls1)
#         print("max value",max(ls1))
#         print("min value",min(ls1))
#     print(type(ls))
# n = int(input("enter number of list :"))
# no_list=[]
# ls1,ls2,ls3=[],[],[]
#
# for i in range(n):
#     e = int(input("enter no. of element of list{} :".format(i + 1)))
#     no_list.append(e)
# print(no_list)
#
# for i in range(len(no_list)):
#     print("list {}".format(i+1))
#     for j in range(no_list[i]):
#         e = int(input("element{} :".format(j+1)))
#         if i==0:
#             ls1.append(e)
#         elif i==1:
#             ls2.append(e)
#         elif i==2:
#             ls3.append(e)
# if n == 1:
#     fun(ls1)
# if n==2:
#     fun(ls1,ls2)
# if n==3:
#     fun(ls1,ls2,ls3)
#######################################################################
def fun(*ls):
    print(ls)

    if n==2:
     ls1.extend(ls2)
     ls1.sort()
     print(ls1)
     print("max value", max(ls1))
     print("min value", min(ls1))

    elif n==3:
        ls1.extend(ls2)
        ls1.extend(ls3)
        ls1.sort()
        print(ls1)
        print("max value",max(ls1))
        print("min value",min(ls1))
    print(type(ls))
n = int(input("enter number of list :"))
no_list=[]
ls1,ls2,ls3=[],[],[]

for i in range(n):
    e = int(input("enter no. of element of list{} :".format(i + 1)))
    no_list.append(e)
print(no_list)

for i in range(len(no_list)):
    print("list {}".format(i+1))
    for j in range(no_list[i]):
        e = int(input("element{} :".format(j+1)))
        if i==0:
            ls1.append(e)
        elif i==1:
            ls2.append(e)
        elif i==2:
            ls3.append(e)
if n == 1:
    fun(ls1)
if n==2:
    fun(ls1,ls2)
if n==3:
    fun(ls1,ls2,ls3)
