# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

import math
import random
bushes = int(input("Enter numb of bushes: "))
berries = [random.randint(10,50) for i in range(bushes)]
print(berries)
max = 0
for i in range(bushes):
    sum = berries[0] + berries[1] + berries[2] 
    if sum > max:
        max = sum
        print(berries[0] + berries[1] + berries[2])
    a = berries.pop()
    berries.insert(0, a)
    print(berries)
print(max)