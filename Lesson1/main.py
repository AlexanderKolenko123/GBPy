#Задание 1
print('Задание 1')
testString= 'some text'
testInt = 1234
testList = ['1', 'test', 3]
print('строка: ', testString)
print('Целое число: ', testInt)
print('Список: ', testList)
str = input('Введите текст')
print('Вы ввели:', str)
str2 = input('Введите текст')
print('Вы ввели:', str2)

#Задание 2
str = input('Введите время в секундах')
if str.isdigit():
    m, s = divmod(int(str), 60)
    h, m = divmod(m, 60)
    print(f'{h:d}:{m:02d}:{s:02d}')
else:
    print('Строка не содержит цифры')

#Задание 3
str1 = input('Введите число')
if str1.isdigit():
    total = (int(str1) + int(str1 + str1) + int(str1 + str1 + str1))
    print("Сумма чисел n + nn + nnn = %d" % total)
else:
    print('Строка не содержит цифры')

#Задание 4
n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

#Задание 5
profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Рентабельность {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

# Задание 6
a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
# Конец