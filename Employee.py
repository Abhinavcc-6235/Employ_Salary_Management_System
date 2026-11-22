from abc import ABC,abstractmethod  # import ABC(Abstarct Main Class)and the abstractmethode

class Employee(ABC):                 #abstract class Employee from ABC
    def __init__(self,name,basic_slary):  #Constructor
        self.name=name                    #public attribute store employee name
        self.__basic_salary=basic_slary   #private atribute store basic salary

    def get_basic_salary(self):             #getter methode give access to the private attribute 
        return self.__basic_salary

    @abstractmethod                       #abstract methode, child class must implement it
    def calculate_salary(self):
        pass

    def display_details(self):            # normal methode shared by all child classes
        print(f'Employee Name:',self.name)
        print(f'Basic salary:',self.get_basic_salary())
