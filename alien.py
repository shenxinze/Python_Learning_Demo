alien_0 = {'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print('You just earned '+str(new_points)+' points!')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('------------------------------------------------')

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

print('The alien is ' + alien_1['color'] + '.')

alien_1['color'] = 'yellow'
print('The alien is now ' + alien_1['color'] + '.')

print('------------------------------------------------')

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x_position: ' + str(alien_2['x_position']))

# alien_2['speed'] = 'fast'

if alien_2['speed'] == 'slow':
	x_increment = 1
elif alien_2['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_2['x_position'] = alien_2['x_position'] + x_increment
print('New x_position: ' + str(alien_2['x_position']))

print('------------------------------------------------')

# 删除键值对
print(alien_2)
del alien_2['y_position']
del alien_2['x_position']
print(alien_2)