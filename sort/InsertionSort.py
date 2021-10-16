def insertion_sort(list):
    for index in range(len(list) - 1):
        for index2 in range(index + 1, 0, -1):
            if list[index2] < list[index2 - 1]:
                list[index2], list[index2 -1] = list[index2 - 1], list[index2]
            else:
                break
    return list



def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        key = list[i]
        while list[j] > key and j >= 0:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = key
    return list
            
        
        


import random

data = random.sample(range(100), 10)
print(insertion_sort(data))