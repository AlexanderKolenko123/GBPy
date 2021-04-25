# Задание 3-1
# **************************************************************************************
def get_division(x, y):
    if y == 0:
        return f"Деление на {y} запрещено"
    else:
        result = x / y
        return result


a = int(input("Введеите делимое \n "))
b = int(input("Введеите делитель \n "))
print(get_division(a, b))


# **************************************************************************************
# Задание 3-2
# **************************************************************************************


def user_info(x_, y_, z_, a_, b_, c_):
    return ', '.join([x_, y_, z_, a_, b_, c_])


name = input('Введи имя \n ')
surname = input('Введи фамилию \n')
year = input('Введи год рождения \n')
city = input('Введи город проживания \n')
email = input('Введи email \n ')
phone = input('Введи телефон \n')

print(user_info(name, surname, year, city, email, phone))


# **************************************************************************************
# Задание 3-3
# **************************************************************************************

def max_sum(x, y, z):
    num = [x, y, z]
    num.sort()
    return num[1] + num[2]


# так же можно использовать  return max(max(a, b), c)
def max_sum2(x, y, z):
    num = max(max(x, y), z)
    return num


arg1 = int(input('Insert 1st digit:\n'))
arg2 = int(input('Insert 2nd digit:\n'))
arg3 = int(input('Insert 3nd digit:\n'))

print(max_sum(arg1, arg2, arg3))
print(max_sum2(arg1, arg2, arg3))


# **************************************************************************************
# Задание 3-4
# **************************************************************************************
def power1(a, n):
    return a ** n


def power2(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n > 0:
        return res
    else:
        return 1 / res


print(f"Function Pow: {pow(3, -3)}")
print(f"Function my 1: {power1(3, -3)}")
print(f"Function my 2: {power2(3, -3)}")


# **************************************************************************************
# Задание 3-5
# **************************************************************************************

def my_summa():
    total = 0
    exit = False

    while exit == False:
        number = input('Введи число или $ для выхода: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == '$':
                exit = True
                break
            else:
                res = res + int(number[el])
        total = total + res
        print(f'Текуща сумма: {total}')
    print(f'Общая сумма: {total}')


my_summa()

# **************************************************************************************
# Задание 3-6
# **************************************************************************************
def int_func(*args):
    text = input("Введи слова: ")
    print(text.title())
    return 0


int_func()

# Другое решение

text = input("Введи слова:")
words = text.split()


def int_func2(my_list):
    temp_str = ''
    for i in range(len(my_list)):
        temp_str = temp_str + my_list[i].capitalize() + ' '
    print(temp_str)
    return 0


int_func2(words)


# **************************************************************************************