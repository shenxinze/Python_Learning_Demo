# 9-6
class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name,self.type)

    def open_restaurant(self):
        print('In operation')

    def set_number_served(self,num):
        self.number_served = num

    def increment_number_served(self,addNum):
        self.number_served += addNum


class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavors = ['flavor1','flavor2','flavor3']

    def show_flavors(self):
        print(self.flavors)


IceCreamStand1 = IceCreamStand('name1','type1')
IceCreamStand1.show_flavors()

# 9-7
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greet_user(self):
        print('Hello,' + self.first_name + ' ' + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.admin = Privileges()
        self.privileges = ['can add post','can delete post','can ban user']

    # def show_privileges(self):
    #     for privilege in self.privileges:
    #         print(privilege)


# admin = Admin('xinze','shen')
# admin.show_privileges()

admin1 = Admin('xz','shen')
admin1.admin.show_privileges()

