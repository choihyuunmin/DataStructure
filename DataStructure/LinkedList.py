class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node Data  :  {self.data}"


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def show(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == None:
            print("No one node")
            return

        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            del tmp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    tmp = node.next
                    node.next = node.next.next
                    del tmp
                    return
                else:
                    node = node.next


if __name__ == "__main__":
    linked_list1 = LinkedList(0)

    for data in range(1, 10):
        linked_list1.add(data)

    linked_list1.show()
    print("---------------")
    linked_list1.delete(0)
    linked_list1.delete(8)
    linked_list1.show()
