'''
def pri(ls):
    for l in ls:
        if type(l) == int:
            print(l)
        if type(l) == str:
            print('\t', l)
        if type(l) == list:
            pri(l)
'''

ls=[0,1,2,['a','b','c'],[4,5,6,'d','e','f'],7,'g',8,'h',9,10,'i','j']
# pri(ls)

for l in ls:
    if type(l) == int:
        print(l)
    if type(l) == str:
        print('\t', l)
    if type(l) == list:
        for ll in l:
            if type(ll) == int:
                print(ll)
            if type(ll) == str:
                print('\t', ll)