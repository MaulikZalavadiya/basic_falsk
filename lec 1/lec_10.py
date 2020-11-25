from lec_9 import fun4

class studentinfo:
    def __init__(self,rollnumber,name):
        self.rollnumber=rollnumber
        self.name=name

class studentmark:
    def __init__(self,rollnumber,m1,m2,m3):
        self.rollnumber=rollnumber
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        ls4 = []

        print(">>>>>>>>>>>>>>", self.obj.noStudent)

        for i in range(self.obj.noStudent):
            avg = (self.marks1[i] + self.marks2[i] + self.marks3[i]) // 3

            ls4.append([str(self.obj.rollno[i]), str(avg)])

        return ls4


class main:
    # std_ls=[]
    # avg_dic=[]
    # a_ls=[]
    rono=[]
    name1=[]
    mark1=[]
    mark2=[]
    mark3=[]
    ls3=[]
    n=int(input("enter no of student:"))
    for i in range(n):

       print("student name %d:" %(i+1))
       rollnumber = int(input("\tenter roll no:"))
       rono.append(rollnumber)
       name = input("\tenter name:")
       name1.append(name)
       m1 = int(input("\tmark1:"))
       mark1.append(m1)
       m2 = int(input("\tmark2:"))
       mark2.append(m2)
       m3 = int(input("\tmark3:"))
       mark3.append(m3)

       ls3.append([str(rollnumber), name])
    s1=studentinfo(rollnumber,name)
    s2=studentmark(rollnumber,m1,m2,m3)
       # avg= s2.avg()
       # std_ls.append(ls_1)
       # avg_dic[rollnumber]=avg
       # a_ls.append(avg)
    # a_ls.sort(reverse=True)
    ls4 = s2.average()
    print(ls3)
    print(ls4)
    fun4(ls3,ls4)
###########################################################################
# from lec_9 import fun4
#
#
# class StudentInfo:
#     def __init__(self, nos, r, n):
#         self.rollno = r
#         self.name = n
#         self.noStudent = nos
#         print("<<<<<<<<<<<<<<<",self.noStudent)
#
#
# class StudentMarks:
#     def __init__(self, objOne, m1, m2, m3):
#         self.obj = objOne
#         self.marks1 = m1
#         self.marks2 = m2
#         self.marks3 = m3
#
#     def average(self):
#         ls4 = []
#
#         print(">>>>>>>>>>>>>>",self.obj.noStudent)
#
#         for i in range(self.obj.noStudent):
#             avg = (self.marks1[i] + self.marks2[i] + self.marks3[i]) // 3
#
#             ls4.append([str(self.obj.rollno[i]), str(avg)])
#
#         return ls4
#
#
# class Main:
#     nos = int(input("Enter n of Students:"))
#     rollno = []
#     name = []
#     marks1 = []
#     marks2 = []
#     marks3 = []
#     ls3 = []
#
#     for i in range(nos):
#         rno = int(input("Enter rollno:"))
#         nam = input("Enter Name:")
#         mark1 = int(input("Enter sub-1 marks:"))
#         mark2 = int(input("Enter sub-2 marks:"))
#         mark3 = int(input("Enter sub-3 marks:"))
#
#         rollno.append(rno)
#         name.append(nam)
#         marks1.append(mark1)
#         marks2.append(mark2)
#         marks3.append(mark3)
#
#         ls3.append([str(rno), nam])
#
#     objOne = StudentInfo(nos, rollno, name)
#
#     objTwo = StudentMarks(objOne, marks1, marks2, marks3)
#
#     ls4 = objTwo.average()
#
#     print(ls3)
#
#     print(ls4)
#
#     fun4()(ls3, ls4)
