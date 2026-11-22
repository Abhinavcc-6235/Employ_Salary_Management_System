from Employee import Employee      #import employee parent class
class  ContractEmployee(Employee):  #ContractEmployee class inherit from vehicle class
    def calculate_salary(self):     #implements the abstract methode from employee
        return (self.get_basic_salary()+(self.get_basic_salary() * 0.05))

