n = int(input("enter no of students:"))
ls=[]
avg_ls=[]
dic={}

def fun1():

    m1 = open("studentinfo.txt", "w+")
    m2 = open("studentmarks.txt", "w+")
    m1.write("rollno\t-\tname\n")
    m2.write("rollno\t-\tm1\t-\tm2\t-\tm3\n")
    for i in range(n):
        print("students name %d:" % (i + 1))
        rollno = int(input("\tenter roll no:"))
        name = input("\tenter name:")
        mark1 = int(input("\tmark1:"))
        mark2 = int(input("\tmark2:"))
        mark3 = int(input("\tmark3:"))

        ls.append("%d"%(i))
        ls[i]=[rollno,mark1,mark2,mark3]
        # total=mark1+mark2+mark3
        m1.write(str(rollno) + "\t-\t" + name + "\n")
        m2.write(str(rollno) + "\t-\t" + str(mark1) + "\t-\t" + str(mark2) + "\t-\t" + str(mark3) + "\n")
        # print("total:",total)
    print(ls)

def fun2():
    sinfo = open("studentinfo.txt", "r")
    smark = open("studentmarks.txt", "r")
    k = sinfo.read()
    k1 = smark.read()
    # print(k)
    # print(k1)
def fun3():
    print("average:")
    for i in range(len(ls)):
        sum=0
        for j in range(1,len(ls[i])):
            sum +=ls[i][j]
        average=sum/3
        print("student{} average :".format(i+1),average)
        dic[i+1]=average
        avg_ls.append(average)
    print(dic)
    print(avg_ls)

def fun4():
    # fls1=[]
    # fls2=[]
    # fls3=[]
    f1=open("studentinfo.txt","r")
    # f2=open("Average.txt","w+")
    print("sort list student")
    # f2=open("Average.txt","w+")
    f3=open("A_grade.txt","w+")
    f4=open("B_grade.txt","w+")
    f5=open("C_grade.txt","w+")
    avg_ls.sort(reverse=True)
    print(avg_ls)
    print(dic)
    line=f1.readlines()
    c=0
    for i in avg_ls:
        for j in dic:
            if i==dic[j]:
                if i>=80 and i<=100:
                    grade="A"
                    f3.write(str(line[j])+"\t-\t"+str(avg_ls[c])+"\t-\t"+grade+ '\n')
                elif i>=60 and i<80:
                    grade="B"
                    f4.write(str(line[j]) + "\t-\t" + str(avg_ls[c]) + "\t-\t" + grade + '\n')
                elif i>=40 and i<60:
                    grade="C"
                    f5.write(str(line[j]) + "\t-\t" + str(avg_ls[c]) + "\t-\t" + grade + '\n')
                else:
                    grade="F"
                print(str(line[j]),end=""); print("\t-\t"+str(avg_ls[c])+"\t-\t"+grade)
                # f2.write(str(line[j])+"\t-\t"+str(avg_ls[c])+"\t-\t"+grade+"\n")
        c+=1

fun1()
fun2()
fun3()
fun4()
##############################################################################################################
# def GetAndStore(fo1, fo2):
#     ls = []
#     for i in range(int(input('Number of students:'))):
#         print(i+1, 'Students details:')
#         ls.append({
#             'rollno': int(input('\tRoll No:')),
#             'name': input('\tName:'),
#             'marks': [int(input('\t\tMarks '+str(i+1)+':')) for i in range(3)]
#         })
#     fo1.writelines(['_'.join([str(ls[i]['rollno']), ls[i]['name']]) + '\n' for i in range(len(ls))])
#     fo1.seek(0, 0)
#     fo2.writelines(['_'.join([str(ls[i]['rollno']), '_'.join([str(i) for i in ls[i]['marks']])]) + '\n' for i in range(len(ls))])
#     fo2.seek(0,0)
#
#
# def ReadData(fo1, fo2):
#     fls1 = [(i[0:len(i)-1]).split('_') for i in fo1.readlines()]
#     fls2 = [(i[0:len(i)-1]).split('_') for i in fo2.readlines()]
#     return [{
#         'rollno': int(fls1[i][0]),
#         'name': fls1[i][1],
#         'marks': [int(fls2[i][j + 1]) for j in range(3)]
#     } for i in range(len(fls1))]
#
#
# def CalcAvg(ls):
#     [i.update(avg=round(sum(i['marks'])/len(i['marks']), 2)) for i in ls]
#     return ls
#
#
# def StoreGrade(ls, fo3, fo4, fo5):
#     ls.sort(key=lambda ls:ls['avg'], reverse=True)
#     fls3, fls4, fls5 = [], [], []
#     for i in ls:
#         line = str('_'.join([str(i['rollno']), i['name'], str(i['avg'])]))+'\n'
#         if 80 <= i['avg'] <= 100:
#             fls3.append(line)
#         elif 60 <= i['avg'] < 80:
#             fls4.append(line)
#         elif 40 <= i['avg'] < 60:
#             fls5.append(line)
#     fo3.writelines(fls3); fo4.writelines(fls4); fo5.writelines(fls5)
#
#
# fo1, fo2, fo3, fo4, fo5 = open('StudentsInfo.txt', 'w+'), open('StudentsMarks.txt', 'w+'), open('A_Grade.txt', 'w+'), open('B_Grade.txt', 'w+'), open('C_Grade.txt', 'w+')
#
# GetAndStore(fo1, fo2)
# data = ReadData(fo1, fo2)
# data = CalcAvg(data)
# StoreGrade(data, fo3, fo4, fo5)
#
# fo1.close(); fo2.close(); fo3.close(); fo4.close(); fo5.close()
