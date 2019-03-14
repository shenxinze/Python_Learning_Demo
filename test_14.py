# 7-4
msg = '\n请输入披萨配料'
while True:
    value = input(msg)
    if value == 'quit':
        break
    else:
        print('我们会在披萨中添加' + value + '.')

# 7-5 && 7-6
tip = '\n请输入您的年龄'
tip += "\n输入'exit'可以退出"
flag = True
while flag:
    age = input(tip)
    if age == 'exit':
        flag = False
        break
    else:
        age = int(age)
    if age < 3:
        print('免费')
    elif (age >= 3) and (age < 12):
        print('10美元')
    else:
        print('15美元')


