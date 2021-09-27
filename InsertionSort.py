def insertion_sort(list):
    for index in range(len(list) - 1):
        for index2 in range(index + 1, 0, -1):
            if list[index2] < list[index2 - 1]:
                list[index2], list[index2 -1] = list[index2 - 1], list[index2]
            else:
                break
    return list



import random

data = random.sample(range(100), 10)
print(insertion_sort(data))