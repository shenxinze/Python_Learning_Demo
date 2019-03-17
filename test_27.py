filename = 'learning_python.txt'

# 第一种 读取全部文件
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print('*********************')

# 第二种 遍历文件对象
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

print('*********************')

# 第三种 存储列表中 with 外部打印
str = ''
with open(filename) as file_object:
    strLines = file_object.readlines()

for line in strLines:
    print(line.rstrip())
    str += line

print('*********************')

# 替换
newStr = str.replace('Python','C')
print(newStr)



