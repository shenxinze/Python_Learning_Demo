class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(self.name,self.type)

    def open_restaurant(self):
        print('In operation')


restaurant = Restaurant('canguan','zaodian')
restaurant_1 = Restaurant('canguan_1','zaodian_1')
restaurant_2 = Restaurant('canguan_2','zaodian_2')
restaurant_3 = Restaurant('canguan_3','zaodian_3')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()


class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greet_user(self):
        print('Hello,' + self.first_name + ' ' + self.last_name)


user_1 = User('xinze','shen')
user_1.describe_user()
user_1.greet_user()