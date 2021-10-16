def binary_search(list, target):
    if len(list) == 1 and target == list[0]:
        return True
    if len(list) == 1 and target != list[0]:
        return False
    if len(list) == 0:
        return False
    
    mid = len(list) // 2
    if target == list[mid]:
        return True
    else:
        if target > list[mid]:
            return binary_search(list[mid:], target)
        else:
            return binary_search(list[:mid], target)
        
data = [1,2,5,6,8,10,16,77,100]
d = binary_search(data, 10)
print(d)
        