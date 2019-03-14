from test_23 import Restaurant
from test_25_1 import User,Privileges,Admin

restaurant = Restaurant('name','type')
restaurant.set_number_served(24)
restaurant.increment_number_served(42)
print(restaurant.number_served)

print('************************')

admin = Admin('xinze','shen')
admin.admin.show_privileges()