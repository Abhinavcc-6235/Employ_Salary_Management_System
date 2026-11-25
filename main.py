from Employee import Employee
from PermanentEmployee import PermanentEmployee   #import permanetemployee class
from ContractEmployee import ContractEmployee     #import contractemployee class
permanentEmp=PermanentEmployee('abhinav',50000)
ContractEmp=ContractEmployee('arjun',60000) 

permanentEmp.display_details()                  #create permanentemployee object
sal1 = permanentEmp.calculate_salary()          
print(f'Salary after bonus = {sal1}')
print('------------------------------')

ContractEmp.display_details()                   #create contractemplyoyee object
sal2 = ContractEmp.calculate_salary()  
print(f'Salary after bonus = {sal2}') 

#output
# Employee Name: abhinav
# Basic salary: 50000
# Salary after bonus = 51000.0
# ------------------------------
# Employee Name: arjun
# Basic salary: 60000
# Salary after bonus = 63000.0
