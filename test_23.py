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


# restaurant = Restaurant('qita','xiaochi')
# restaurant.set_number_served(24)
# restaurant.increment_number_served(42)
# restaurant.increment_number_served(33)
# print(restaurant.number_served)


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


# user = User('xinze','shen')
# 加一
# user.increment_login_attempts()
# print(user.login_attempts)
# 置0
# user.reset_login_attempts()
# print(user.login_attempts)