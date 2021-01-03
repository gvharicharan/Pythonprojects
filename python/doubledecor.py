def decorfun(fun):
    def inner():
        result=fun()
        return result*6
    return inner
@decorfun

def num():
    return 7

print(num())
