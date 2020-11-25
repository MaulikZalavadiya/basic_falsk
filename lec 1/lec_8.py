# n = int(input("enter no of line:"))
# def fun1(n):
#     file=open("mb.txt","w+")
#     for i in range(n):
#         m=input("enter line %d:" %(i+1))
#         file.write(m +"\n")
#     file.close()
# fun1(n)
# def fun2():
#     w=0
#     l=0
#     file = open("mb.txt", "r")
#     for n in file:
#       l += 1
#       words = n.split(' ')
#       w = w + len(words)
#     print("total line:",l)
#     print("total word:", w)
#     print("total char",file.seek(0,2))
# fun2()
#######################################################################
def fun1():
    n=int(input("enter no of line:"))
    fo=open("1.txt","w+")
    for i in range(n):
        m=input("enter filedata:")
        fo.write(m + "\n")
fun1()
def fun2():
    fo=open("1.txt","r")
    # str = fo.read()
    d=fo.readlines()[::-1]
    # d=str.replace("hello","hi")
    # k=fo.readline()
    # print(k)
    fo1=open("2.txt","w")
    #d=fo.write(d[::-1])
    fo1.writelines(d)
    # fo1.writelines(d)
fun2()
##################################################################################
