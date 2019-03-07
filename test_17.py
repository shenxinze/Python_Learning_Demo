def make_shirt(size,msg='I love Python'):
    print('这件T恤的尺寸是' + size + ',' + '字样是"' + msg + '"。')


# make_shirt('33','believe you can do it')
# make_shirt(msg='believe you can do it',size='35')
make_shirt('45')
make_shirt('40')
make_shirt('39','Focus on the present')


def describe_city(city,country="China"):
    print(city.title() + '在' + country.title())


describe_city('北京')
describe_city('上海')
describe_city('纽约','美国')
