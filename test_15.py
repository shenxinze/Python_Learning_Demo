# 7-8
# sandwich_orders = ['sandwich1','sandwich2','sandwich3']
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print('I made your tuna ' + sandwich)
#     finished_sandwiches.append(sandwich)
# print(sandwich_orders)
# print(finished_sandwiches)


# 7-9
sandwich_orders = ['pastrami','sandwich1','sandwich2','pastrami','sandwich3','pastrami']
print('The deli is out of pastrami')
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your tuna ' + sandwich)
    finished_sandwiches.append(sandwich)

print(sandwich_orders)
print(finished_sandwiches)

# 7-10
tip = 'If you could visit one place in the world, where would you go?'
while True:
    address = input(tip)
    print(address)
    break
