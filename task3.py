# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1 1.2 3.1 5 10.01] => 0.19

array = input('Ведите вещественные числа через пробел: ').split()


length=0
fractional_list=[]
for i in range(len(array)):
    num='0.'+array[i].partition('.')[2]
    if num!='0.':
        fractional_list.append(num)
    if len(num)>length+2:
        length=len(num)-2

my_list = list(map(float, fractional_list))
max=my_list[0]
min=my_list[0]
for j in range(len(my_list)):
    if my_list[j]>max:
        max=my_list[j]
    if my_list[j]<min:
        min=my_list[j]

print(f'Разница между максимальным ({max}) значением дробной части и минимальным ({min}) составляет {round((max-min), length)}')

