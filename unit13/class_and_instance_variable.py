class Employee:
  companyName = "Apple"  #class variable
  noOfEmployees = 0      #class variable
  
  def __init__(self, name):
    self.name = name             #instance variable
    self.raise_amount = 0.02     #instance variable
    Employee.noOfEmployees +=1   
    
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India" 
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()