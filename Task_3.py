# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list=[1, 2, 1, 3, 4]
print(list)

for i in range(len(list)-1):
    for j in range(i+1,len(list)-1):
        if(list[i]==list[j]):
            list.pop(j)
print(list)
    
