class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
            
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
            
        
    def search(self, key):
        return self._search_value(self.root, key)
    
    def _search_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._search_value(root.left, key)
        else:
            return self._search_value(root.right, key)

    
    
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    
    def _delete_value(self, node, key):
        if node == None:
            return node, False
        
        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_vaule(node.right, key)
        return node, deleted
    



if __name__ == '__main__':
    array = [10, 30, 40, 60, 70, 20, 50, 90, 110]
    
    tst = BinarySearchTree()
    for i in array:
        tst.insert(i)
        
    print(tst.search(10))
    
        
    