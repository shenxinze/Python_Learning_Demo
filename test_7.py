car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi' ? I predict False.")
print(car == 'audi')

print('-----------------')
print('str' == 'stre')
print('str' == 'str')

print('Str' == 'str')
print('Str'.lower() == 'str')

num = 10
print(num == 10)
print(num > 12)
print(num < 12)
print(num <= 12)
print(num >= 12)
print(num != 12)

age = 18
if age > 0 and age <= 18:
	print('未成年')
else:
	print('成年人')

true1 = True
true2 = False
if true1 or true2:
	print('至少有一个 True')

nums = [1,2,3,4,5,6,7,8,9,0]
total1 = 2
total2 = 12
if total1 in nums:
	print('total 在列表中')

if total2 not in nums: 
	print('total 不在列表中')