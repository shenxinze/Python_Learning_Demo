dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 元祖中的元素不可以修改 下面操作会报类型错误
# dimensions[0] = 250

print('Original dimensions:')
for dimension in dimensions:
	print(dimension)

# 可以重新对元祖赋值，这个是可行的
dimensions = (400,100)
print('\nModified dimensions')
for dimension in dimensions:
	print(dimension)


