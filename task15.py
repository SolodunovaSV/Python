# Пользователь вводит одно число N. 
# Далее идут N чисел, записанных на новой строчке каждое. 
# Вывести максимальное и минимальное (циклы)
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# import random


# num = random.randint(5, 10)
# min_num = 15
# max_num = 1
# for i in range(num):
#     kg = random.randint(1, 15)
#     if kg < min_num:
#         min_num = kg
#     elif kg > max_num:
#         max_num = kg

# print(min_num)
# print(max_num)

import random


num = random.randint(5, 10)


kg = random.randint(1, 15)
min_num_kg = kg
max_num_kg = kg
for _ in range(num - 1):
    kg = random.randint(1, 15)
    if kg < min_num_kg:
        min_num_kg = kg
    elif kg > max_num_kg:
        max_num_kg = kg
print(min_num_kg)
print(max_num_kg)