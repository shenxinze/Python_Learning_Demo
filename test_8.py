# 5-3
# alien_color = 'green'
# if alien_color == 'green':
# 	print('The player gets 5 gold pieces!')

# alien_color = 'red'
# if alien_color == 'green':

# 5-4	
# alien_color = 'green'
# if alien_color == 'green':
# 	print('The player gets 5 gold pieces!')
# else:
# 	print('The player gets 10 gold pieces!')

# alien_color = 'yellow'
# if alien_color == 'green':
# 	print('The player gets 5 gold pieces!')
# else:
# 	print('The player gets 10 gold pieces!')

# 5-5
# alien_color = 'yellow'
# if alien_color == 'green':
# 	print('The player gets 5 gold pieces!')
# elif alien_color == 'yellow':
# 	print('The player gets 10 gold pieces!')
# elif alien_color == 'red':
# 	print('The player gets 15 gold pieces!')

# 5-6
age = 89
if age < 2:
	status = '婴儿'
elif age >= 2 and age < 4:
	status = '蹒跚学步'
elif age >= 4 and age < 13:
	status = '儿童'
elif age >= 13 and age < 20:
	status = '青少年'
elif age >= 20 and age < 65:
	status = '成年人'
elif age >= 65:
	status = '老年人'

if age >= 2 and age < 4:
	print('他正在'+status+'。')
else:
	print('他是个'+status+'。')
	
# 5-7
favorite_fruits = ['香蕉','西瓜','圣女果']
if '香蕉' in favorite_fruits:
	print('你真的很喜欢'+'香蕉'+'!')
if '西瓜' in favorite_fruits:
	print('你真的很喜欢'+'西瓜'+'!')	
if '圣女果' in favorite_fruits:
	print('你真的很喜欢'+'圣女果'+'!')
if '草莓' not in favorite_fruits:
	print('你不喜欢'+'草莓'+'!')
if '芒果' not in favorite_fruits:
	print('你不喜欢'+'芒果'+'!')