def greet_users(names):
    # 向列表中的每一位用户都发出简单的问候
    for name in names:
        msg = 'hello,' + name.title() + '!'
        print(msg)


usernames = ['hannah','ty','margot']
greet_users(usernames)