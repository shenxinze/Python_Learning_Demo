info_1 = {
	'first_name': 'cheng',
	'last_name': 'xia',
	'age': 26,
	'sex': 1,
	'city': 'zhengzhou'
}
info_2 = {
	'first_name': 'shen',
	'last_name': 'dekuan',
	'age': 29,
	'sex': 2,
	'city': 'zhengzhou'
}
info_3 = {
	'first_name': 'shen',
	'last_name': 'aixia',
	'age': 3,
	'sex': 2,
	'city': 'zhengzhou'
}
people = [info_1,info_2,info_3]
for people in people:
	print(people)

print('----------------------------')

pet1 = {
	'owner': 'ming',
	'type': 'dog'
}
pet2 = {
	'owner': 'wang',
	'type': 'cat'
}
pets = [pet1,pet2]
for pet in pets:
	print(pet)

print('----------------------------')

favorite_places = {
	'小王': ['云南'],
	'小李': ['西藏','青岛','山东'],
	'小张': ['三亚','哈尔滨']
}

for name,places in favorite_places.items():
	print(name.title() + ',喜欢的地方是：')
	for place in places:
		print(place)

print('----------------------------')

nums = {
	'a': [1,2],
	'b': [4,7,8],
	'c': [4,66,78],
	'd': [0,1],
	'e': [66,99]
}

for name,nums in nums.items():
	print(name.title() + ',喜欢的数字是：')
	for num in nums:
		print('\t' + str(num))

print('----------------------------')

cities = {
	'北京': {
		'owner': '中国',
		'num': '200',
		'story': '1'
	},
	'上海': {
		'owner': '中国',
		'num': '200',
		'story': '2'
	}
}

for city,infos in cities.items():
	print(city)
	for name,info in infos.items():
		print(name)
		print(info)