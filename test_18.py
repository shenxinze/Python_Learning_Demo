def city_country(city,country):
    print(city.title() + '，' + country.title())


city_country('上海','中国')
city_country('纽约','美国')
city_country('北京','中国')


def make_album(name,musicName,total="1"):
    info = {
        '姓名': name,
        '歌曲': musicName,
        '数量': total
    }
    print(info)
    return info


make_album('周杰伦','不能说的秘密')
make_album('周杰伦','说好的幸福',3)

while True:
    name = input('请输入歌手姓名(退出请输入“q”)：')
    if name == 'q':
        break
    musicName = input('请输入该歌手的歌曲名称(退出请输入“q”)：')
    if musicName == 'q':
        break
    make_album(name,musicName)
