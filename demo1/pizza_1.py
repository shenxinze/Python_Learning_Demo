# from user_profile import build_profile
from user_profile import build_profile as shen # 设置别名


def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# user_profile = build_profile('albert','einstein',location='princeton',field='physics')
# print(user_profile)


user_profile = shen('albert','einstein',location='princeton',field='physics')
print(user_profile)
