for num in range(1,21):
	print(num)

nums = list(range(1,1000001))
# for num in nums:
# 	print(num)

print(min(nums))
print(max(nums))
print(sum(nums))

print('-----------------------')

oddNumbers = list(range(1,21,2))
# print(oddNumbers)
for n in oddNumbers:
	print(n)

print('-----------------------')

num3 = []
for value in range(3,30):
	if value % 3 == 0:
		num3.append(value)
print(num3)
for num in num3:
	print(num)

print('-----------------------')

numbers3 = [value**3 for value in range(1,11)]
# print(numbers3)
for num in numbers3:
	print(num)