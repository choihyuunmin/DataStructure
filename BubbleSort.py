def bubble_sort(list):
    for index in range(len(list) - 1):
        swap = False
        for index2 in range(len(list) - index - 1):
            if list[index2] > list[index2 + 1]:
                list[index2], list[index2 + 1] = list[index2 + 1], list[index2]
                swap = True
        if swap == False:  # swap을 안해도 되면 미리 loop를 빠져나옴
            break  
    return list
        
        
        

def bubble_sort2(list):
    length = len(list) - 1
    for i in range(length):
        for j in range(length - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list




        
import random
data = random.sample(range(100), 50)
print(bubble_sort(data))