# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# Ряд чисел Фибоначчи:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 
# 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …

# num = input('Введите натуральное число: ') #1

# while not num.isdigit():
#     print('Вы ввели не число')
#     num = input('Введите натуральное число: ')
# num = int(num)
# fib1 = 0
# fib2 = 1
# fib = 1
# count = 2
# while fib < num:
#     fib = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib
#     count += 1
# if fib == num:
#     print(count)
# else:
#     print(-1)



num = input('Введите натуральное число: ') #2

while not num.isdigit():
    print('Вы ввели не число')
    num = input('Введите натуральное число: ')
num = int(num)
fib1 = 0
fib2 = 1
count = 2
while fib2 < num:
    fib2, fib1 = fib1 + fib2, fib2
    count += 1
if fib2 == num:
    print(count)
else:
    print(-1)