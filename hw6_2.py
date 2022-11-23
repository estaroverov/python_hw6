# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import math
#Предыдущий вариант решения:
numbers = input("Введите числа через пробел: ").split()
def ListOddSum(numbers):
    counter = 0
    sum = 0
    for i in numbers:
        if counter % 2 != 0:
            sum += int(i)
        counter += 1
    return sum

print("Summ1: ", ListOddSum(numbers))
##############################################
# Улучшенный вариант

lo_sum = lambda numbers: sum([y for x,y in enumerate(map(int,numbers)) if x%2!=0])
print("Summ2: ", lo_sum(numbers))