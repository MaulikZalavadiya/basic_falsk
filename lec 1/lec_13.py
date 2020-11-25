class HDFC:
    def __init__(self, amount):
        self.max_amount = 20000
        self.amount = amount

    def withdraw(self):
        if self.amount <= self.max_amount:
            print("withdraw complete")
        else:
            for i in range(3):
                if self.amount >= self.max_amount:
                     pass

                elif i == 3:
                    print("Your 3 Chances Is Finish!")
                    exit()
                else:
                    self.amount = int(input("Enter Amount 20000 or less:"))


class AXIS:
    def __init__(self, amount):
        self.max_amount = 30000
        self.amount = amount

    def withdraw(self):
        if self.amount < self.max_amount:
            pass
        else:
            for i in range(5):
                if self.amount >= self.max_amount:
                    pass

                elif i == 5:
                    print("Your 5 Chances Is Finish!")
                    exit()
                else:
                    self.amount = int(input("Enter Amount 30000 or less:"))


class ATM:
    bank = input("enter bank name HDFC or AXIS:")
    Amount = int(input("enter amount:"))
    if bank=="HDFC":
        hb=HDFC(Amount)
        hb.withdraw()
    else:
        ab=AXIS(Amount)
        ab.withdraw()