# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120

# n = input('Введите число N: ')

# while not n.isdigit():
#     print('Вы ввели не число')
#     n = input('Введите число N: ')

# n = int(n)
# fact = 1

# while n > 1:
#     fact *= n
#     n -= 1

# print(fact)

n = input("Введите целое число N: ")

while not n.isdigit():
    print("Вы ввели не число")
    n = input("Введите целое число N: ")

n = int(n)
fact = 1

while n > 1:
    fact *= n
    n -= 1

print(fact)