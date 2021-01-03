class Programmer:

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setSalary(self,sal):
        self.salary=sal

    def getSalary(self):
        return self.salary

    def setTechnologies(self,techs):
        self.technologies=techs

    def getTechnologies(self):
        return self.technologies
p1=Programmer()
p1.setName('Charan')
p1.setSalary(100000)
p1.setTechnologies(["Java","Hibernate","Spring","Python"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())
