names = ['a','b','c','d','admin']
if names:
	for name in names:
		if name == 'admin':
			print('Hello admin,would you like to see a status report?')
		else:
			print('Hello '+name+', thank you for logging in again.')	
else:
	print('We need to find some users!')

print('---------------------')

current_users = ['a1','b1','c1','d1','e1','JOHN']
new_users = ['a1','c1','f1','g1','h1','john']

current_users = [value.lower() for value in current_users]
new_users = [value.lower() for value in new_users]

for new_user in new_users:
	if new_user in current_users:
		print('请输入其他的用户名')
	else:
		print('这个用户名未被使用')

print('---------------------')

nums = [value for value in range(1,10)]
for nums in nums:
	if nums == 1:
		print(str(nums) + 'st')
	elif nums == 2:
		print(str(nums) + 'nd')
	elif nums == 3:
		print(str(nums) + 'rd')
	else:
		print(str(nums) + 'th')