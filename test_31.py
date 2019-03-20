class Employee():
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.Raise = 5000

    def give_raise(self):
        self.salary += self.Raise
        return self.salary
