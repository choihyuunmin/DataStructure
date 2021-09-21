import queue


data1 = queue.Queue()
data2 = queue.LifoQueue()
data3 = queue.PriorityQueue()

data3.put((1, "Choi"))
data3.put((4, "ccong"))
data3.put((8, "min"))

print(data3.qsize())
print(data3.get())  # 우선순위가 높은 것부터 나옴(1 > 4 > 8)

#-----------------------------------------------------------------------------


list_queue = list()

def enqueue(data):
    list_queue.append(data)

def dequeue():
    de_data = list_queue[0]
    del list_queue[0]
    return de_data

for ddata in range(10):
    enqueue(ddata)
    
print(list_queue)
print(dequeue())
print(list_queue)
print(dequeue())
print(list_queue)
print(dequeue())
print(list_queue)