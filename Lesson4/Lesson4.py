# Задание 4-1
# **************************************************************************************

from sys import argv
import random
from functools import reduce
from itertools import count
from itertools import cycle
from math import factorial

name, time, salary, extraBonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(extraBonus)
    result = time * salary + bonus
    print(f'заработная плата сотрудника {name} = {result}')
except ValueError:
    print(' args values not a number')

# **************************************************************************************
# Задание 4-2
# **************************************************************************************

listLen = int(input('Введи количество элементов в списке\n'))
randRange = int(input('Введи диапазон чисел\n'))
originList = []

for i in range(listLen):
    originList.append(random.randint(1, randRange))

print(f'исходный список:{originList}')
newList = [item for i, item in enumerate(originList) if originList[i - 1] < originList[i]]
print(f'новый  список:{newList}')

# **************************************************************************************
# Задание 4-3
# **************************************************************************************

print(f'{[item for item in range(20, 240) if item % 20 == 0 or item % 21 == 0]}')

# **************************************************************************************
# Задание 4-4
# **************************************************************************************

origin_list = [10, 12, 8, 22, 8, 3, 8, 11, 123, 500]
new_list = [item for item in origin_list if origin_list.count(item) == 1]
print(new_list)

# **************************************************************************************
# Задание 4-5
# **************************************************************************************

print(f'четный список {[item for item in range(99, 1001) if item % 2 == 0]}')
print(f'результат умножения  {reduce(lambda x, y: x * y, [item for item in range(99, 1001) if item % 2 == 0])}')

# **************************************************************************************
# Задание 4-6
# **************************************************************************************

for item in count(int(input('Введите начало списка '))):
    print(item)
    if item > 3000:
        break

num = 0
tempList = [True, 'ABC', 123, None]
for item in cycle(tempList):
    print(item)
    num += 1
    if num > 100:
        break


# **************************************************************************************
# Задание 4-7
# **************************************************************************************
def factorial_generator() -> object:
    for item in count(1):
        yield factorial(item)


x = 0
for i in factorial_generator():
    if x < 5:
        print(i)
        x += 1
    else:
        break
# **************************************************************************************
