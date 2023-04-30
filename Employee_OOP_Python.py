class Employee:
    increment=1.5
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    def increase(self):
        self.salary=self.salary*Employee.increment

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount
    @classmethod
    def from_str(cls,empstring):
        fname,lname,salary=empstring.split("-")
        return(cls(fname,lname,salary))
    
    @staticmethod
    def isOpen(day):
        if(day=='sunday'):
            return False
        elif(day=='saturday'):
            return False
        else:
            return True

class Programmer(Employee):
    progIncrement=2.0
    def __init__(self,fname,lname,salary,proglang):
        super().__init__(fname,lname,salary)
        self.proglang=proglang
    def increase(self):
        self.salary=(self.salary*Programmer.progIncrement)
        

e1=Employee('Manan','Pandya',5500.0)
e2=Employee('Sumit','Badgujar',5600.0)

e1.increase()
e2.increase()
print(e1.fname+" "+e1.lname)
print(e2.fname+" "+e2.lname)
print(e1.salary)
print(e2.salary)

print(e1.__dict__)

e1.change_increment(1.8)
e1.increase()
print(e1.__dict__)

e3=Employee.from_str("Sai-Kumar-6500.60")
print(e3.__dict__)

print(e1.isOpen('monday'))
print(e1.isOpen('sunday'))

p1=Programmer('Harsh','Shukla',3450.0,'Java Spring Boot')
print(p1.__dict__)
p1.increase()
print(p1.__dict__)
print(p1.isOpen('saturday'))

