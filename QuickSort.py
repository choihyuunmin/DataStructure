# pivot = 기준점


def quick_sort(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort2(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return quick_sort2(left) + [pivot] + quick_sort2(right)


import random

data = random.sample(range(100), 10)

test = quick_sort(data)
test2 = quick_sort2(data)

print(test)
print(test2)
