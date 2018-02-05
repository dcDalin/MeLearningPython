# Creating and instanciating simple classes

# Classes allow us to logically group our data and function in a way thats easy to reuse 
# and build upon if need be

# methods -> function associated with a class

# class we could use as a blueprint for creating employee

'''
    Class is a blueprint for creating instances
    Each unique employee that we create using our employee class
    will be the instance of a class Employee
''' 


class Employee:
    ''' 
        init method as initialize or constructor 
        When we create methods within a class, they receive the instance as the first argument automatically
        by convention, we call the instance self
        we can specify other arguments after self
    '''
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Dalin', 'Oluoch', 100000)

print(emp_2.fullname())

print(Employee.fullname(emp_1))