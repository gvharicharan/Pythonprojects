"""class Student:
    def __init__(self):
        self.__id=453
        self.__name='Charan'

    def display(self):
        print(self.__id)
        print(self.__name)

s=Student()
s.display()
print(s._Student__id);"""


'''class Student:
    def setId(self,id):
        self.id=id

    def getId(self):
        return self.id

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

s=Student()
s.setId(406)
s.setName('charan')
print(s.getId())
print(s.getName())'''


#ASSIGNMENT
class Patient:
    def setId(self,id):  #@ReservedAssignment
        self.__id=id

    def getId(self):
        return self.__id

    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name

    def setSsn(self,ssn):
        self.__ssn=ssn

    def getSsn(self):
        return self.__ssn


p=Patient()
p.setId(789)
p.setName('Hari charan')
p.setSsn(754)
print(p.getId())
print(p.getName())
print(p.getSsn())
