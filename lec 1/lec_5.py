#qus1

# n=input("enter no of elemement:")
# lst=[]
# ls1=[]
# ls2=[]
# sum=0
# sum1=0
# sum2=0
# ls =n.split(",")
# for i in ls:
#     if(i.isdigit()==True):
#         lst.append(int(i))
# print(lst)
#
# for i in range(len(lst)):
#     sum+=lst[i]
# print(sum)
# if sum %2 is not 0:
#      print("total sum is odd number")
# elif sum %2 is 0:
#      for i in range(len(lst)):
#         if lst[i]%2 is 0:
#            ls2.append(lst[i])
#         else:
#            ls1.append(lst[i])
#      ls1.sort()
#      ls2.sort()
#      # print(ls1)
#      # print(ls2)
#      for j in range(len(ls1)):
#          sum1=sum1+ls1[j-1]
#      for k in range(len(ls2)):
#          sum2 += ls2[k - 1]
#
#      while sum1!=sum2:
#          if sum1>sum2:
#              x=int(len(ls1))
#              y=ls1[int(x/2-1)]
#              ls2.append(y)
#              ls1.pop(int(x/2-1))
#              ls2.sort()
#              sum1=0
#              sum2=0
#              for i in range(len(ls1)):
#                  sum1=sum1+ls1[i-1]
#              for j in range(len(ls2)):
#                  sum2+=ls2[j-1]
#
#
#          elif sum1 < sum2:
#                  x = int(len(ls2))
#                  y = ls2[int(x / 2 - 1)]
#                  ls1.append(y)
#                  ls2.pop(int(x / 2 - 1))
#                  ls1.sort()
#                  sum1 = 0
#                  sum2 = 0
#                  for i in range(len(ls1)):
#                      sum1 = sum1 + ls1[i - 1]
#                  for j in range(len(ls2)):
#                      sum2 += ls2[j - 1]
#      print(ls1)
#      print(ls2)
#      print("sum of ls1:",sum1)
#      print("sum of ls2:",sum2)

######################################################################

# ls=[0,8,4,12,2,12,4,9,1,3,5,13,3]
# ls1=[]
# ls2=[]
# total=sum(ls)
# ls.sort(reverse=-1)
# if total%2==0:
#     for i in ls:
#         if sum(ls1)<sum(ls2):
#             ls1.append(i)
#         else:
#             ls2.append(i)
# print(ls1)
# print(ls2)
# print(sum(ls1))
# print(sum(ls2))


######################################################################
#qus2

# n=input("enter a no of elemenet:")
# lst=[]
# ls1=[]
#
# lst1=n.split(",")
# for i in lst1:
#     if i.isdigit() is True:
#         lst.append(int(i))
# x=0
# ls1=[]
# while x<len(lst):
#     ls2=[lst[x]]
#     for i in range(x+1,len(lst)):
#         if ls2[-1]<=lst[i]:
#             ls2.append(lst[i])
#         else:
#             break
#     ls1.append(ls2)
#     x+=1
#
# n=0
# for i in range(len(ls1)):
#     if len(ls1[n])<len(ls1[i]):
#         n=i
# print(ls1[n])


##########################################################################################
# ls=[]
# n=int(input("enter a no of element:"))
# for i in range(n):
#     ls.append(int(input("enter a number:")))
# print(ls)
#
# ls1=[]
# ls2=[ls1]
#
# for i in ls:
#     if len(ls1)==0:
#         ls1.append(i)
#     elif ls2[-1][-1]<i:
#         ls2[-1].append(i)
#     else:
#         ls2.append([i])
# print(ls2)
# print(max(ls2,key=len))

####################################################################

## qus3


ls,ls1,ls2,ls3=[],[],[],[]
val1=int()
val2=int()
n=int(input("enter no of one list:"))
for i in range(n):
      ls.append(int(input("enter a element:")))
      val1 += ls[i] * 10 ** (n - i - 1)
print(" ",ls)
print(" ",val1)
m=int(input("enter no of second list:"))
for i in range(m):
    ls1.append(int(input("enter a element:")))
    val2 += ls1[i] * 10 ** (m - i - 1)
print(" ",ls1)
print(" ",val2)
sum=val1+val2
mul=val1*val2
print("sum:",sum)
print("mul:",mul)
for i in str(sum):
    ls2.append(int(i))
for i in str(mul):
    ls3.append(int(i))
print(" ",ls2)
print(" ",ls3)
# #############################################################################
# ls1=[int(input('Enter a N1 Number:')) for i in range(int(input('Enter a N1 Value:')))]
# ls2=[int(input('Enter a N2 Number:')) for i in range(int(input('Enter a N2 Value:')))]
# print(ls1, ls2)
# print([int(i) for i in str(int(''.join([str(i) for i in ls1])) + int(''.join([str(i) for i in ls2])))])
# print([int(i) for i in str(int(''.join([str(i) for i in ls1])) * int(''.join([str(i) for i in ls2])))])