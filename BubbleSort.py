def bubble_sort(list):
    for index in range(len(list) - 1):
        swap = False
        for index2 in range(len(list) - index - 1):
            if list[index2] > list[index2 + 1]:
                list[index2], list[index2 + 1] = list[index2 + 1], list[index2]
                swap = True
                
        if swap == False:
            break  
    return list
        
        
        
        
        
import random
data = random.sample(range(100), 50)
print(bubble_sort(data))