class Employee:
    # class variables
    num_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):  # (constructor)
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # class function, takes in the current instance of the class as its input
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    # this decorator allows you to modify the class itself
    # usually they are used as optional constructors, esp if you want to pass __init__ inputs
    # that are in alternative formates
    def set_raise_amt(cls, amount):
        # takes in the class as an inputs
        cls.raise_amount = amount

    @staticmethod
    # do not take in class instances or the class itself as inputs.
    # all data it accesses depends solely on whatever input you put in.
    def is_weekday(day):
        # no reference of cls or self
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    @fullname.setter #{}.setter --> {} needs to refer to a pre-exiting attribute, not a METHOD!!
    def full__name(self,name): #def {}(args) -->{} will be the method name when calling this setter, ie. class_instance.{} = args
        first,last = name.split(" ")
        self.first = first
        self.last = last


A = Employee("B","C",1000)
print(A.fullname)
A.full__name = "D E" #setter function
print(A.fullname) #one of the methods!!
A.first = "F" #setter function
print(A.fullname) #one of the methods!!

# inheritence:

class Developer(Employee):
    # class child_class(parent_class)
    def __init__(self, first, last, pay, prog_lang=None):
        super().__init__(first, last, pay)
        """
        super().__init__(first,last,pay) 
        --> references the init method in Employee and passes the args 
    
        """
        if not prog_lang:
            self.prog_lang = []
            # default val is set to None, you dont want mutable data as the default value!
        else:
            self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def show_emp(self):
        for emp in self.employees:
            print(emp.fullname())

"""
    dunder functions:
allow you to perfom functions/actions on the class. 

__init__ --> constructor
__str__ --> usually used to produce useful info from the class. USE: str(class_instance) or class_instance.__str__()
__repr__ --> prints the class and its example/expected inputs USE: repr(class_instance) or class_instance.__repr__() eg. repr(mngr_1) --> OUTPUT: "Manager(first, last, pay, employeesList)"
__add__ --> denotes what happens or is added when you add two class objects together. ie eg. mnger_1 + mnger_2 =?, could be it added their salaries together? or employee list? or emails? 
__len__ --> produces length of a variable/string/object.

    decorator:

    1. @property


allows you to use a class method as a class attribute
eg. 
    class A()
        def B()
            pass
    
    C = A
    C.B() --> this expects a method, which is correct!!
    
    class A()
        @property
        def B()
            pass
    
    C.B --> same call as above, you called the method like an attribute, which is the function of '@property"

    2. @{attribute}.setter
allows you to change or set the attribute {} to any value

    3. @{attribute}.getter

    4.@{attribute}.deleter







dev_1=Developer("A","B",5000,"Python")
dev_2=Developer("C","D",1000,"Cython")

mng_1 = Manager("e","f",60000,[dev_1,dev_2])
dev_3=Employee

"""

