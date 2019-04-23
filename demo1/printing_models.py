"""
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)


# print(unprinted_designs)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
"""


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
# print_models(unprinted_designs[:], completed_models) # 创建副本，传递副本进入函数，可以保留原始的列表
show_completed_models(completed_models)
print(unprinted_designs)
