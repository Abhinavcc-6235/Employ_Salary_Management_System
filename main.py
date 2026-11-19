from Employee import Employee
from PermanentEmployee import PermanentEmployee
from ContractEmployee import ContractEmployee
permanentEmp=PermanentEmployee('abhinav',50000)
ContractEmp=ContractEmployee('arjun',60000) 

permanentEmp.display_details()
sal1 = permanentEmp.calculate_salary()
print(f'Salary after bonus = {sal1}')
print('------------------------------')

ContractEmp.display_details()
sal2 = ContractEmp.calculate_salary()  
print(f'Salary after bonus = {sal2}') 