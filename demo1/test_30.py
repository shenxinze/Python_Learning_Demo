import json

# filename = 'favorite_number.json'


# def favorite_number():
#     number = input('输入你喜欢的数字：')
#     with open(filename,'w') as f_obj:
#         json.dump(number,f_obj)
#     read_number()
#
#
# def read_number():
#     with open(filename) as f_obj:
#         number = json.load(f_obj)
#         print("I know your favorite number! It’s " + number + '!')


def get_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        number = input('输入你喜欢的数字：')
        with open(filename,'w') as f_obj:
            json.dump(number,f_obj)
    else:
        print("I know your favorite number! It’s "+number+'!')


# favorite_number()
get_favorite_number()
