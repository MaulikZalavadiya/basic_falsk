import random

class Bankinfo:
    def __init__(self, fn, ln, gender, address):
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = address


class Account:
    def __init__(self, ac_no, amount):
        self.ac_no = ac_no
        self.amount = amount


class saving(Account):

    min = 10000
    rate = 6


    def validate(self):
        if self.amount >= self.min:
            pass
        else:
            for i in range(3):
                if self.amount >= self.min:
                    pass

                elif i == 3:
                    print("Your 3 Chances Is Finish!")
                    exit()
                else:
                    self.amount = int(input("Enter Amount 10000 or Above:"))

    def intrestCalculate(self, month):
        year = month / 12
        interest = float((self.amount * self.rate * year) / 100)
        print(interest)
        return interest


class current(Account):

    min = 5000
    rate = "None"


    def validate(self):
        if self.amount >=self.min:
            pass
        else:
            for i in range(3):
                if self.amount >=self.min:
                    pass

                elif i == 3:
                    print("Your 3 Chances Is Finish!")
                    exit()
                else:
                    self.amount = int(input("Enter Amount 10000 or Above:"))



class main():

    fn = input("enter first name:")
    ln = input("enter last name:")
    gender = input("enter gender:")
    addres = input("enter address:")
    acno = random.randint(0000000000000, 9999999999999)
    print("account number:", acno)
    amount = int(input("enter amount:"))
    BI = Bankinfo(fn, ln, gender, addres)
    BA = Account(acno, amount)

    ac_type = input("Enter ac typr S and C:-")
    if ac_type == "S":
        s1 = saving(acno, amount)
        s1.validate()

        month = int(input("Enter Your Months:"))

        interest = s1.intrestCalculate(month)

        print("Your First Name Is: ", BI.fn)
        print("Your Last Name Is: ", BI.ln)
        print("Your Gender Is: ", BI.gender)
        print("Your Address Is: ", BI.address)
        print("Your Account No Is:", BA.ac_no)
        print("Your Amount Is:", BA.amount)
        print("Your Interest Is: ", interest)

    elif ac_type == "C":

        c = current(acno, amount)

        c.validate()

        month = int(input("Enter Your Month:"))

        print("No Interest Available For Current Account !")

        print("Your First Name Is: ", BI.fn)
        print("Your Last Name Is: ", BI.ln)
        print("Your Gender Is: ", BI.gender)
        print("Your Address Is: ", BI.address)
        print("Your Account No Is:", BA.ac_no)
        print("Your Amount Is:", BA.amount)
        print("No Interest In Current Account..")



