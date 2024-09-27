'''
4.Create a class Employee where:
  Each employee has an instance variable salary.
  There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
  Write a method total_salary that calculates the total salary for an employee (including the bonus).
  Exercise:
   >Create several employee instances with different salaries.
   >Change the bonus amount (static variable) and see how it affects all employees.
   >Calculate and print the total salary for each employe
'''
class Employee:
    
    bonus = 1000

    
    def __init__(self, salary):
        self.salary = salary
    
    
    def total_salary(self):
        total = self.salary + Employee.bonus
        return f"Total Salary: {total}"

employee1 = Employee(5000)
employee2 = Employee(7000)
employee3 = Employee(9000)


print(f"Employee 1: {employee1.total_salary()}")  
print(f"Employee 2: {employee2.total_salary()}")  
print(f"Employee 3: {employee3.total_salary()}")  

Employee.bonus = 2000


print(f"Employee 1: {employee1.total_salary()}")  
print(f"Employee 2: {employee2.total_salary()}")  
print(f"Employee 3: {employee3.total_salary()}")  
