student={}
n=int(input("enter the student range :"))

for i in range(n):
    no=int(input("enter roll no:"))
    name=input("enter name:")
    marke=int(input("enter marke:"))
    student["no"+str(i)]=no
    student["name"+str(i)]=name
    student["marke"+str(i)]=marke

print(student)