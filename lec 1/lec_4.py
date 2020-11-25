# ls1=[]
# ls2=[]
# a=input("enter value:")
# print(a)
# ls=a.split(",")
# print(ls)
# for i in ls:
#     if((i.isdigit())==True):
#         ls1.append(int(i))
#     else:
#         ls2.append(i)
# print("list1:",ls1)
# print("list2:",ls2)
# print("max:",max(ls1))
# print("min:",min(ls1))
# ls2.reverse()
# print(ls2)
#
# new one
student={"s1":{
    'roll no':int(input("enter roll no:")),
    'name':input("enter name:"),
    'marks':int(input("enter marks:")),
    'grade':"none"},
"s2":{
    'roll no':int(input("enter roll no:")),
    'name':input("enter name:"),
    'marks':int(input("enter marks:")),
    'grade':"none"},
"s3":{
    'roll no':int(input("enter roll no:")),
    'name':input("enter name:"),
    'marks':int(input("enter marks:")),
    'grade':"none"}}
print(student.items())
for i,j in student.items():
      for x,y in j.items():
          if x=="marks":
              if y>80and y<=100:
                  j['grade']="A"
              elif y>=60 and y<=80:
                  j['grade']="B"
              elif y>=40 and y<60:
                  j['grade']="c"
print(student)
# print(type(student))
