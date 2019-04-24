cars = ['bmw','audi','toyota','subaru']
# cars.sort()
# print(cars)

# cars.sort(reverse = True)
# print(cars)

# print('Here is the original list:')
# print(cars)

# print('\nHere is the sorted list:')
# print(sorted(cars))

# print('\nHere is the ogiginal list again:')
# print(cars)

# print(cars)
# cars.reverse()
# print(cars)

length = len(cars)
print(length)

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())		

print('---------------------------')

num = 'shen'
print(num == 'Shen')
print(num.title() == 'Shen')
print(num)