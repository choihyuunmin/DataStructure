import random

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

    def delete(self, data):
        searched = False
        self.current_node = self.head
        self.parent = self.head

        while self.current_node:
            if self.current_node.data == data:
                searched = True
                break
            elif data < self.current_node.data:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False

        # Case1 (삭제할 Node가 Leaf Node)
        if self.current_node.left == None and self.current_node.right == None:
            if data < self.parent.data:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        # Case2 (삭제할 Node가 Child Node를 한 개 가질 경우)
        if self.current_node.left and self.current_node.right == None:
            if data < self.parent.data:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right:
            if data < self.parent.data:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # Case3 (삭제할 Node가 Child Node를 두 개 가질 경우)
        if self.current_node.left and self.current_node.right:
            if data < self.parent.data:  # Case3-1 (Parent Node 오른쪽에 삭제할 Node 있을 때)
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left

                if self.change_node.right:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None

                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                self.change_node_parent.left = None

                if self.change_node.right:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.change_node_parent
                self.change_node.left = self.change_node.left

        return True


if __name__ == "__main__":

    numbers = set()
    while len(numbers) != 100:
        numbers.add(random.randint(0, 999))
        
    head = Node(500)
    bt = NodeManage(head)
    for num in numbers:
        bt.insert(num)
        
    for num in numbers:
        if not bt.search(num):
            print("SEARCH FAILED", num)
            
    print(numbers)
    
     