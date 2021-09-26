def selection_sort(list):
    for stand in range(len(list) - 1):
        lowest = stand
        for index in range(stand + 1, len(list)):
            if list[lowest] > list[index]:
                lowest = index
        list[lowest], list[stand] = list[stand], list[lowest]
    return list

 


import random

data = random.sample(range(100), 10)

print(data)
print(selection_sort(data))