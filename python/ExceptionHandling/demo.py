import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)


try:
    f=open("myFile",'w')
    a,b=[int(x) for x in input("Enter two numbers").split()]
    logging.info("Division in progress")
    c=a/b
    print(c)
    f.write('writting %d into file' %c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("please enter a non zero value")
    logging.error("Division by zero")

else:
    print("you have entered a non zero number")
finally:
    f.close()
    print("file closed")
    print("code after exception")
