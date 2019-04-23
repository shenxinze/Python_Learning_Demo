my_foods = ['pizza','falafel','carrot cake']

print('The first three foods in the list are:')
for food in my_foods[:3]:
	print(food)

print('-------------------')

print('Three foods from the middle of the list are:')
for food in my_foods[1:3]:
	print(food)

print('-------------------')

print('The last three foods in the list are:')
for food in my_foods[-3:]:
	print(food)

print('-------------------')

my_nums = [1,2,3]
friend_nums = my_nums[:]

my_nums.append(4)
friend_nums.append(5)

print('My list of Numbers is:')
for nums in my_nums:
	print(nums)

print('My friend list of Numbers is:')
for nums in friend_nums:
	print(nums)