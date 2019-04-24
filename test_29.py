# 10-6
"""
def add():
    try:
        num1 = int(input('请输入一个数字'))
        num2 = int(input('请输入另一个数字'))
        total = num1 + num2
    except ValueError:
        print('你输入的格式有问题')
    else:
        print(total)


add()
"""

# 10-7
"""
while True:
    try:
        num1 = int(input('请输入一个数字'))
        num2 = int(input('请输入另一个数字'))
        total = num1 + num2
    except ValueError:
        print('你输入的格式有问题')
    else:
        print(total)
"""

# 10-8
try:
    with open('cats.txt') as cat:
        print(cat.read())
    with open('a/dogs.txt') as dog:
        print(dog.read())
except FileNotFoundError:
    # print('沒有找到文件')
    pass

# 10-9
try:
    with open("the.txt") as book:
        content = book.read()
        number = content.lower().count('the')
        print(number)
except FileNotFoundError:
    pass


