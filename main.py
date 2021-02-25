############3strings

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# st = 'as 23 fdfdg544'
# res = ''
# for i in st:
#     if i.isdigit():
#         res += i
# res = ','.join(res)
# print(res)


# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
# res = ''
# for item in st:
#     if item.isdigit():
#         res += item
#     else:
#         res += '!'
# res = res.strip('!').split('!')
# res = [i for i in res if i]
# res = ','.join(res)
# print(res)


############list comprehension


# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# greeting1 = [i.upper() for i in greeting]
# print(greeting1)

# 2
# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# num = [i ** 2 for i in range(0, 50) if i % 2 != 0]
#
# print(num)

################## function

# - створити функцію яка виводить ліст
# a = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]

# def lis(a):
#     print(a)
#
#
# lis(a)

# - створити функцію яка приймає три числа та виводить та повертає найменше.
# def func(a, b, c):
#     min = 0
#     if a <= b and a <= c:
#         min = a
#     elif b <= a and b <= c:
#         min = b
#     elif c <= a and c <= b:
#         min = c
#     return min


# print(func(45, 123, 67))

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def func(a, b, c):
#     max = 0
#     if a >= b and a >= c:
#         max = a
#     elif b >= a and b >= c:
#         max = b
#     elif c >= a and c >= b:
#         max = c
#     return max
#
#
# print(func(455, 123, 67))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def func(*args):
#     maxNum = args[0]
#     min = args[0]
#     for i in args:
#         if i <= min:
#             min = i
#         if i >= maxNum:
#             maxNum = i
#     print(maxNum)
#     return min
#
# func(45, 23, 67, 3,1243)

# - створити функцію яка виводить ліст
# def func(lis):
#     print(lis)
#
# func([1,2,3,4])

# - створити функцію яка повертає найбільше число з ліста
# def func(lis):
#     print(max(lis))
#
# func([1,2,67,3,4])

# - створити функцію яка повертає найменьше число з ліста
# def func(lis):
#     print(min(lis))
#
# func([-23,1,2,67,3,4])

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def func(lis):
#     print(sum(lis))
#
# func([1,2,67,3,4,5])

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def func(lis):
#     print(sum(lis) / len(lis))
#
#
# func([1, 2, 67, 3, 4, 5])

# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення

# def decor(func):
#     def wrap():
#         return func().replace('_', ' ')
#     return wrap
#
# @decor
# def pr():
#     return 'Hello_boss_!!!'
#
#
# print(pr())
