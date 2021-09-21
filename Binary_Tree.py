class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class NodeManage:
    """
    if data >= Parent Node  -> right
    else data < Parent Node  -> left

    """

    def __init__(self, head):
        self.head = head

    def insert(self, data):
        self.current_node = self.head
        while True:
            if data < self.current_node.data:
                if self.current_node.left:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(data)
                    break
            else:
                if self.current_node.right:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(data)
                    break

    def search(self, data):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.data == data:
                return True
            elif data < self.current_node.data:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False


if __name__ == "__main__":
    head = Node(1)

    BinaryST = NodeManage(head)
    BinaryST.insert(2)
    BinaryST.insert(4)
    BinaryST.insert(7)
    BinaryST.insert(8)
    BinaryST.insert(9)
    
    print(BinaryST.search(4))
