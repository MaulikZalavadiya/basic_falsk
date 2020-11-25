import re

class singup:
    def __init__(self,fn,ln,un,pwd):
        self.fn = fn
        self.ln = ln
        self.un = un
        self.pwd = pwd
class singin(singup):
    def __init__(self, Sing_Up, un, pwd):
        self.un = un
        self.pwd = pwd
        self.Sing_Up=Sing_Up

    def validate(self):
        try:

            if self.pwd == self.Sing_Up.pwd:
                print("Welcome", self.un)


            else:

                raise pwdNotMatched

                pass

        except pwdNotMatched :

            print("Password does not Match, Access Denied!!!")




class Error(Exception):
    pass


class PwdIsNull(Exception):

    pass


class PwdTooSmall(Exception):

    pass


class PwdTooLarge(Exception):

    pass


class SmallLetter(Exception):

    pass


class BlockLetter(Exception):

    pass


class OnlyOneDigit(Exception):

    pass


class SpecialChar(Exception):

    pass


class pwdNotMatched(Exception):

    pass
class main:

    fn=input("enter first name:")
    ln=input("enter last name:")
    un=input("enter username:")
    pwd=input("enter password")
    try:
        if len(pwd)==0:
           raise PwdIsNull

           pass
        elif len(pwd) < 8:
            raise PwdTooSmall

            pass
        elif len(pwd) > 16:
            raise PwdTooLarge

            pass
        elif not re.search("[a-z]" , pwd):
            raise SmallLetter

            pass
        elif not re.search("[A-z]" , pwd):
            raise BlockLetter
            pass
        elif not re.search("[0-9]" , pwd):

             raise OnlyOneDigit

             pass
        elif not re.search("[!@#$%^&*]" , pwd):
              raise SpecialChar
              pass

    except PwdIsNull:
        print("enter password compulsary")
        print()
    except PwdTooSmall:
        print("password is small.")
        print()
    except PwdTooLarge:
        print("password is large.")
        print()
    except SmallLetter:
        print("password does not contain small letter.")
        print()
    except BlockLetter:
        print("Password does not contain block letter.")
        print()
    except OnlyOneDigit:
        print("enter more than one digit")
        print()
    except SpecialChar:
        print("password does not contain allowed special character")
        print()

    Sing_Up = singup(fn, ln, un, pwd)
    un = input("Enter Username: ")
    pwd = input("Enter Password: ")
    Sing_In = singin(Sing_Up,un,pwd)
    Sing_In.validate()
#################################################################################3
# class SignUp:
#     def __init__(self, signUpFirstName, signUpLastName, signUpUserName, signUpPassword):
#         self.signUpFirstName = signUpFirstName
#         self.signUpLastName = signUpLastName
#         self.signUpUserName = signUpUserName
#         self.signUpPassword = signUpPassword
#
#
# class SignIn:
#     def __init__(self, signUpObejct, signInUserName, signInPassword):
#         self.signInUserName = signInUserName
#         self.signInPassword = signInPassword
#         self.signUpObejct = signUpObejct
#
#     def loginCheck(self):
#         try:
#             if self.signUpObejct.signUpUserName == self.signInUserName and self.signUpObejct.signUpPassword == self.signInPassword:
#
#                 print("Welcome {} {} !".format(self.signUpObejct.signUpFirstName, self.signUpObejct.signUpLastName))
#             else:
#                 raise LoginError
#
#         except LoginError:
#
#             print("Username or Password is incorrect !")
#
#
# class MinimumCharError(Exception):
#     pass
#
#
# class MaximumCharError(Exception):
#     pass
#
#
# class OneLowerCaseError(Exception):
#     pass
#
#
# class OneUpperCaseError(Exception):
#     pass
#
#
# class OneDigitError(Exception):
#     pass
#
#
# class OneSpecialCharError(Exception):
#     pass
#
#
# class LoginError(Exception):
#     pass
#
#
# class Main:
#     def __init__(self):
#         digit = False
#         lower = False
#         upper = False
#
#         print("Enter Value for SignUp:")
#
#         signUpFirstName = input("Enter Firstname:")
#         signUpLastName = input("Enter Lastname:")
#         signUpUserName = input("Enter Username:")
#
#         while True:
#             try:
#                 signUpPassword = input("Enter Password:")
#
#                 if len(signUpPassword) < 8:
#                     raise MinimumCharError
#
#                 if len(signUpPassword) > 16:
#                     raise MaximumCharError
#
#                 for i in signUpPassword:
#                     if i.islower():
#                         lower = True
#                         break
#                 if not lower:
#                     raise OneLowerCaseError
#
#                 for i in signUpPassword:
#                     if i.isupper():
#                         upper = True
#                         break
#                 if not upper:
#                     raise OneUpperCaseError
#
#                 for k in signUpPassword:
#                     if k.isdigit():
#                         digit = True
#                         break
#                 if not digit:
#                     raise OneDigitError
#
#                 flag = False
#                 for i in signUpPassword:
#                     if 32 <= ord(i) <= 47:
#                         flag = True
#                         break
#                     if 58 <= ord(i) <= 64:
#                         flag = True
#                         break
#                     if 91 <= ord(i) <= 96:
#                         flag = True
#                         break
#                     if 123 <= ord(i) <= 126:
#                         flag = True
#                         break
#                     else:
#                         flag = False
#                 if not flag:
#                     raise OneSpecialCharError
#
#                 break
#
#             except MinimumCharError:
#
#                 print("This value is too small, try again!")
#
#                 print()
#
#             except MaximumCharError:
#
#                 print("This value is too Big, try again!")
#
#                 print()
#
#             except OneLowerCaseError:
#
#                 print("Password contain atleast one lowerCharecter, try again!")
#
#                 print()
#
#             except OneUpperCaseError:
#                 print("Password contain atleast one upperCharecter, try again!")
#
#                 print()
#
#             except OneDigitError:
#
#                 print("Password contain atlist one Digit, try again!")
#
#                 print()
#
#             except OneSpecialCharError:
#
#                 print("Password contain atlist one Special Character, try again!")
#
#                 print()
#
#         signUpObejct = SignUp(signUpFirstName, signUpLastName, signUpUserName, signUpPassword)
#         print("Enter Value for signin:")
#
#         signInUserName = input("Ënter Username:")
#         signInPassword = input("Enter Password:")
#
#         signInObject = SignIn(signUpObejct, signInUserName, signInPassword)
#
#         signInObject.loginCheck()
#
#
# objectMain = Main()
#
