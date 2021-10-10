def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Index is :", index)
    else:
        print("Index is None")
        