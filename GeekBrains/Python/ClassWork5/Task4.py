# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def Enter(numb):
    if numb == 0:
        return " "
    else:
        a = input()
        return a+ Enter(numb - 1) 

print(Enter(2))     




