# 从一个模块中导入多个类
"""
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
"""


# 导入整个模块
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

"""
导入模块中的所有类
语法:
    from module_name import * 
不建议这么做 导入多个类 可以直接导入整个模块，使用 modul_name.class_name 语法访问类
"""


