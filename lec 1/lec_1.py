
str="this is string example"
print(str)
# print("\n")
#
# #reverse string
# str1="this is string example"[::-1]
# print(str1)
# print("\n")

#split string
art=str.split(" ")
print(art)
print("\n")

#wordwise reverse
a=(art[0][::-1])
print(a)
b=(art[1][::-1])
print(b)
c=(art[2][::-1])
print(c)
d=(art[3][::-1])
print(d)
print(a+"\t"+b+"\t"+c+"\t"+d)
print("\n")

# #interchange
print(art[0][0:2][::-1]+ art[0][2:4][::-1])
print(art[1][0:2][::-1])
print(art[2][0:2][::-1]+ art[2][2:4][::-1]+art[2][4:6])
print(art[3][0:2][::-1]+ art[3][2:4][::-1]+art[3][4:6]+art[3][6:8])


print("\n")
# #join string
s="*"
print(s.join(art))
print("\n")
# #replace word
print("this"+str[4:].replace("is","was"))
