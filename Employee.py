from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,basic_slary):
        self.name=name
        self.__basic_salary=basic_slary

    def get_basic_salary(self):
        return self.__basic_salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print(f'Employee Name:',self.name)
        print(f'Basic salary:',self.get_basic_salary())
