# Пользователь вводит число N (1 ≤ N ≤ 10). 
# Далее построчно N чисел от -50 до 50. 
# Нужно вывести наибольшее количество идущих подряд положительных чисел.
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

num = input('Введите число: ')
while num not in '1, 2, 3, 4, 5, 6, 7, 8, 9, 10':
    print('Вы ввели некорректное число')
    print('Ввведите число')
num = int(num)

count = 0
max_count = 0
for t in range(num):
    tem = int(input('Введите значения от -50 до 50: '))
    if tem > 0:
        count += 1
    elif tem <= 0:
        count = 0
    if count > max_count:
        max_count = count

print(max_count)