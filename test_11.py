info = {
	'first_name': 'cheng',
	'last_name': 'xia',
	'age': 26,
	'sex': 1,
	'city': 'zhengzhou'
}

'''
print(info['first_name'])
print(info['last_name'])
print(info['age'])
print(info['sex'])
print(info['city'])
'''

for value in info.values():
	print(value)

nums = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5
}

'''
print('A favorite number is ' + str(nums['a']) + '.')
print('B favorite number is ' + str(nums['b']) + '.')
print('C favorite number is ' + str(nums['c']) + '.')
print('D favorite number is ' + str(nums['d']) + '.')
print('E favorite number is ' + str(nums['e']) + '.')
'''

for key,value in nums.items():
	print(key.title() + ' favorite number is ' + str(value) + '.')


words = {
	'study': '学习，研究；课题；书房',
	'python': '巨蟒；大蟒',
	'good': '好处；善行；慷慨的行为'
}

'''
print('study: ' + words['study'])
print('python: ' + words['python'])
print('good: ' + words['good'])
'''

words['set'] = '去重'
words['key'] = 'k值'
words['value'] = 'value值'
for key,value in words.items():
	print(key + ':' + value)

'''
print('study:\n' +'  '+ words['study'])
print('python:\n' +'  '+ words['python'])
print('good:\n' +'  '+ words['good'])
'''

for key,value in words.items():
	print(key + ':\n' + value)

print('\n---------------------------\n')

# 6-5
rivers = {
	'changjiang': 'China',
	'huanghe': 'China',
	'lancangjiang': 'China'	
}

for river,country in rivers.items():
	print('The '+ river.title() +' runs through '+ country +'.')

for river in rivers.keys():
	print(river)

for country in rivers.values():
	print(country)

print('\n---------------------------\n')

# 6-6
people = {
	'A': 'Python',
	'B': 'JavaScript',
	'C': 'Php'
}

for people in people.keys():
	print(people + '感谢参与')

if 'D' not in people:
	print('邀请您来参与')