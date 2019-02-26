nameArr = ['小红','小明','小爱','小艺']
print('邀请' + nameArr[0] + '与我共进晚餐')
print('邀请' + nameArr[1] + '与我共进晚餐')
print('邀请' + nameArr[2] + '与我共进晚餐')
print('邀请' + nameArr[3] + '与我共进晚餐')

print(nameArr[2])
nameArr.pop(2)
nameArr.insert(2,'小娜')
print(nameArr)

print('邀请' + nameArr[0] + '与我共进晚餐')
print('邀请' + nameArr[1] + '与我共进晚餐')
print('邀请' + nameArr[2] + '与我共进晚餐')
print('邀请' + nameArr[3] + '与我共进晚餐')

print('\n----找到一个更大的餐桌----\n')

nameArr.insert(0,'a')
nameArr.insert(3,'b')
nameArr.append('c')

print('邀请' + nameArr[0] + '与我共进晚餐')
print('邀请' + nameArr[1] + '与我共进晚餐')
print('邀请' + nameArr[2] + '与我共进晚餐')
print('邀请' + nameArr[3] + '与我共进晚餐')
print('邀请' + nameArr[4] + '与我共进晚餐')
print('邀请' + nameArr[5] + '与我共进晚餐')
print('邀请' + nameArr[6] + '与我共进晚餐')

print('\n----只能邀请两位嘉宾----\n')

print(nameArr.pop() + ',我很抱歉，无法邀请你来共进晚餐。')
print(nameArr.pop() + ',我很抱歉，无法邀请你来共进晚餐。')
print(nameArr.pop() + ',我很抱歉，无法邀请你来共进晚餐。')
print(nameArr.pop() + ',我很抱歉，无法邀请你来共进晚餐。')
print(nameArr.pop() + ',我很抱歉，无法邀请你来共进晚餐。')

print('邀请' + nameArr[0] + '与我共进晚餐')
print('邀请' + nameArr[1] + '与我共进晚餐')

del nameArr[0]
del nameArr[0]
print(nameArr)

