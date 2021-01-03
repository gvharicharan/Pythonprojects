class OverTheLimitException(Exception):
    def __init__(self,msg):
        self.msg=msg




def Withdrawl(amount):
    if (amount>500):
        raise OverTheLimitException("you cannot withdraw morethan 500$ ")


Withdrawl(600)
