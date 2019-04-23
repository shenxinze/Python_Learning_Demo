def show_magicians(names):
    for name in names:
        print(name.title())


magic_list = ['a','b','c','d']
# show_magicians(magic_list)

"""
def make_great(names):
    for i in range(0,len(names)):
        names[i] = 'the Great ' + names[i].title()


make_great(magic_list)
show_magicians(magic_list)
"""
def make_great(names):
    change_list = []
    for name in names:
        change_list.append('the Great ' + name.title())
    return change_list


change_list = make_great(magic_list)
show_magicians(change_list)
show_magicians(magic_list)

