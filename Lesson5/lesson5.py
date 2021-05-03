# Задание 5-1
# **************************************************************************************

test_file = open('file_5_1.txt', 'w')
line = input('Введи текст \n')
while line:
    test_file.writelines(line)
    line = input('Введи текст \n')
    if not line:
        break

# **************************************************************************************
# Задание 5-2
# **************************************************************************************

test_file = open('file_5_2.txt', 'r')
content = test_file.read()
print(f'Внутри: \n {content}')
test_file = open('file_5_2.txt', 'r')
content = test_file.readlines()
print(f' - {len(content)}')
test_file = open('file_5_2.txt', 'r')
content = test_file.readlines()
for i in range(len(content)):
    print(f'Символов в строке {i + 1} -  {len(content[i])}')
test_file = open('file_5_2.txt', 'r')
content = test_file.read()
content = content.split()
print(f'Количество слов - {len(content)}')
test_file.close()

# **************************************************************************************
# Задание 5-3
# **************************************************************************************

with open('file_5_3.txt', 'r') as test_file:
    salary = []
    tmp = []
    _list = test_file.read().split('\n')
    for i in _list:
        i = i.split()
        print(i)
        if int(i[1]) < 20000:
            tmp.append(i[0])
        salary.append(i[1])
print(f'< 20000 {tmp}, average {sum(map(int, salary)) / len(salary)}')

# **************************************************************************************
# Задание 5-4
# **************************************************************************************

russian = {'one': 'Один', 'two': 'Два', 'three': 'Три', 'four': 'Четыре'}
test_file = []
with open('file_5_4.txt', 'r') as file:
    for i in file:
        i = i.split(' ', 1)
        test_file.append(russian[i[0]] + ' ' + i[1])
    print(test_file)

with open('file_5_4_ru.txt', 'w') as file2:
    file2.writelines(test_file)


# **************************************************************************************#
# Задание 5-5
# # **************************************************************************************

def test_func():
    with open('test_file_5_6.txt', 'w+') as file:
        line = input('Введи цифры через пробел \n')
        file.writelines(line)
        tmp = line.split()
        print(sum(map(int, tmp)))


test_func()
# # **************************************************************************************
# Задание 5-6
# # **************************************************************************************

subj = {}
with open('file_5_6.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        print(line)
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')

# # **************************************************************************************
# Задание 5-7
# # **************************************************************************************
import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_5_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')

# # **************************************************************************************
