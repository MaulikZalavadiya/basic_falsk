from lec_9 import fun4


class StudentInfo:
    def __init__(self, nos, r, n):
        self.rollno = r
        self.name = n
        self.noStudent = nos
        print("<<<<<<<<<<<<<<<",self.noStudent)


class StudentMarks:
    def __init__(self, objOne, m1, m2, m3):
        self.obj = objOne
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def average(self):
        ls4 = []

        print(">>>>>>>>>>>>>>",self.obj.noStudent)

        for i in range(self.obj.noStudent):
            avg = (self.marks1[i] + self.marks2[i] + self.marks3[i]) // 3

            ls4.append([str(self.obj.rollno[i]), str(avg)])

        return ls4


class Main:
    nos = int(input("Enter No of Students:"))
    rollno = []
    name = []
    marks1 = []
    marks2 = []
    marks3 = []
    ls3 = []

    for i in range(nos):
        rno = int(input("Enter rollno:"))
        nam = input("Enter Name:")
        mark1 = int(input("Enter sub-1 marks:"))
        mark2 = int(input("Enter sub-2 marks:"))
        mark3 = int(input("Enter sub-3 marks:"))

        rollno.append(rno)
        name.append(nam)
        marks1.append(mark1)
        marks2.append(mark2)
        marks3.append(mark3)

        ls3.append([str(rno), nam])

    objOne = StudentInfo(nos, rollno, name)

    objTwo = StudentMarks(objOne, marks1, marks2, marks3)

    ls4 = objTwo.average()

    print(ls3)

    print(ls4)

    fun4(ls3, ls4)
