from Employee import Employee
class  ContractEmployee(Employee):
    def calculate_salary(self):
        return (self.get_basic_salary()+(self.get_basic_salary() * 0.05))

