"""try:
    num=int(input("Enter a even number"))
    assert num%2==0, "You have entered a invalid input or odd number"
except AssertionError as obj:
    print(obj)
print("After the assertion")"""

#ASSIGNMENT
password=input("Enter the password").split()
class Password_ValidationException(Exception):
    def __init__(self,msg):
        self.msg=msg
if len(password)<8:
    raise Password_ValidationException("password should contain atleast 8 characters")
