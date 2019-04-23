users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton'
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris'
	}
}

for username,user_info in users.items():
	print('\nUserName: ' + username)
	full_name = user_info['first'] + ' ' + user_info['last']
	location = user_info['location']

	print('\tFull_name: ' + full_name.title())
	print('\tLocation: ' + location.title())