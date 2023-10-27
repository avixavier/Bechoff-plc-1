class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'
        self.pay = pay
    @property


    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):                      #returns a more user friendly instance address
        return "Employee('{}','{}','{}')".format(self.first,self.last, self.pay)

    def __str__(self):
        return '{}-{}'.format(self.fullname(),self.email)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())




emp_1 = Employee('Corey', 'Schafer', 50000)
print(emp_1)
print(emp_1.email)
# emp_1 = Developer('Corey', 'Schafer', 50000, 'Python')
# dev_2 = Developer('Test', 'Employee', 60000, 'Java')
#
# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
#
# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# # mgr_1.remove_emp(dev_2)
#
# mgr_1.print_emps()
print(str.__add__('a','b'))