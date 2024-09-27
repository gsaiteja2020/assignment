'''
2.Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
  Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
  Exercise:
   >Create multiple employee instances.
   >Print the total number of employees after adding each new employee.
   >Check whether changing the total_employees in one instance affects the others.
'''
class Company:
    
    total_employees = 0
    
    def __init__(self, name, department):
        self.name = name
        self.department = department

        Company.total_employees += 1
    
    def display_employee(self):
        return f"Employee Name: {self.name}, Department: {self.department}"
    
    @staticmethod
    def get_total_employees():
        return f"Total Employees: {Company.total_employees}"
        

employee1 = Company("Alice", "Engineering")
print(Company.get_total_employees())  

employee2 = Company("Bob", "Marketing")
print(Company.get_total_employees())  

employee3 = Company("Charlie", "HR")
print(Company.get_total_employees())  

# Check whether changing the total_employees in one instance affects the others
employee1.total_employees = 100  # Changing static variable for employee1

print(employee1.get_total_employees())  
print(employee2.get_total_employees())  
print(employee3.get_total_employees())  

