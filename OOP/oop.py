class Employee:
    # class variables
    num_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):  # (constructor)
        self.first = first
        self.last = last
        self.pay = pay

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

        if not employees:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


upto https: // youtu.be/RSl87lqOXDE?list = PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc & t = 787
