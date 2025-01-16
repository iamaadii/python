class Employee:
    company = 'Apple'
    def show(self):
        print(f'Name is {self.name} and company is {self.company}')
    
    @classmethod  #decorator 
    def changecomp(cls,newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = 'veer'
e1.show()
e1.changecomp("tesla")
e1.show()
print(Employee.company)
Employee.changecomp("suzuki")
e1.show()
print(Employee.company)