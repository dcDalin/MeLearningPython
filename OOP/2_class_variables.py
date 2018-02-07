'''
    Class variables are variables shared among all instances of a class
    Instance can be unique for each instance e.g. name, email, pay
    Class variables should be the same among each class

    Methods automatically take in the instance which we call self by convention
'''
class Employee:
    # class variable
    raise_amount = 1.04

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + ' ' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # when accessing class variables, we need to do it using the class itself
        # or instance of the class
        #  self.pay = int(self.pay * raise_amount)  <-- raise amount won't work
        #  self.pay = int(self.pay * Employee.raise_amount) or below will also work
        self.pay = int(self.pay * self.raise_amount)
        

emp_1 = Employee('Dalin', 'Oluoch', 100000)
emp_2 = Employee('Hannah', 'Montana', 20000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)