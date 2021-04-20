#Задание 2-1

testList = [123, 'test', 'four', 1 > 3, 2.5]
for elem in testList:
    print(type(elem))

#Задание 2-2

elemCount = int(input('Insert element list count'))
tempList = []
iterator = 0

while iterator < elemCount:
    tempList.append(int(input('Insert list element')))
    iterator += 1
print(tempList)

if len(tempList) % 2 != 0:
    tempList[:-1:2], tempList[1:-1:2] = tempList[1:-1:2], tempList[:-1:2]
else:
    tempList[::2], tempList[1::2] = tempList[1::2], tempList[::2]

print(tempList)

#Задание 2-3

month = int(input('Insert number of month'))
monthList = ['winter', 'spring', 'summer', 'autumn']
monthDict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}

if month == 1 or month == 2 or month == 12:
    print(monthList[0])
    print(monthDict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(monthList[1])
    print(monthDict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(monthList[2])
    print(monthDict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(monthList[3])
    print(monthDict.get(4))
else:
    print('No month found')

#Задание 2-4

tempStr = input('Insert some words separated via space')
tempDict = {}
for i in range(len(tempStr.split())):
    tempWord = tempStr.split();
    if len(tempWord[i]) <= 10:
        tempDict[i] = tempWord[i]
    else:
        tempDict[i] = tempWord[i][:10]
print(tempDict)

#Задание 2-5

tempList = [7, 5, 3, 3, 2]
print(tempList)
tempVal = int(input("Insert numbers from 0 to 100 and 101 for exit "))
while tempVal != 101:
    tempList.insert(0, tempVal)
    tempList.sort(reverse=1)
    print(tempList)
    tempVal = int(input("Insert numbers from 0 to 100 and 101 for exit "))


# Задание 2-6

goodsStructure = []
goodsNum = 0
goodsParams = {'name': '', 'price': '', 'quantity': '', 'units': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'units': []}

def funcAnalytics(x):
    print(f'\n Goods analytics \n {"-" * 30}')
    analysDict = dict(
        {'name': x.get('name'), 'price': x.get('price'), 'quantity': x.get('quantity'),
         'units': x.get('units')})
    return analysDict

while True:
    tempStr = input('Press + to insert  goods params, insert a for analytics view, press e to exit')
    if tempStr == 'e':
        break
    goodsNum += 1
    if tempStr == 'a':
        print(funcAnalytics(analytics))
    elif tempStr == '+':
        for tmp in goodsParams.keys():
            params = input(f'insert {tmp}: ')
            goodsParams[tmp] = params
            analytics[tmp].append(goodsParams[tmp])
        goodsStructure.append((goodsNum, goodsParams))
        print(goodsStructure)
    else:
        print('Incorrect input')



