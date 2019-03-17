filename = 'guest.txt'

"""
name = input('请输入你的名字： ')

with open(filename,'w') as file_object:
    file_object.write(name + '\n')
"""

while True:
    name = input("请输入你的名字(输入'q'退出)： ")
    if name == 'q':
        break
    else:
        print('Hello,' + name + '!')
        with open(filename,'a') as file_object:
            file_object.write(name.lstrip() + '\n')

