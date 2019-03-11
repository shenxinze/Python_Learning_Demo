from printing_models import print_models,show_completed_models
# import pizza_2
# from pizza_2 import make_pizza
# from pizza_2 import make_pizza as shen
# import pizza_2 as fn
from pizza_2 import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# pizza_2.make_pizza(12)
# make_pizza(12)
# shen(32)
# fn.make_pizza(34)
make_pizza(46)