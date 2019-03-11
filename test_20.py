def make_sanwich(*ingredients):
    print(str(ingredients)+' have been added into sanwiches.')


make_sanwich('salad')
make_sanwich('chicken','turkey')
make_sanwich('cabbage','chicken','hotdog')


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile


user_info = build_profile('xinze','shen',sex = '男',age = '27')
print(user_info)


def make_car(make_factory,type,**information):
    cars = {}
    cars['make-factory'] = make_factory
    cars['type'] = type
    for key,value in information.items():
        cars[key] = value
    return cars


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

