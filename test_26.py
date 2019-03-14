from collections import OrderedDict
from random import randint

words = OrderedDict()

words['study'] = '学习，研究；课题；书房'
words['python'] = '巨蟒；大蟒'
words['good'] = '好处；善行；慷慨的行为'

for key,value in words.items():
    print(key + ': ' + value)

print('***************************')


class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self,type):
        self.sides = type
        n = 1
        while n <= 10:
            print(randint(1,self.sides))
            n += 1


# die_6 = Die()
# die_6.roll_die(6)

# die_10 = Die()
# die_10.roll_die(10)

die_20 = Die()
die_20.roll_die(20)


