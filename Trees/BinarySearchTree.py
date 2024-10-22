class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if current_node.value > value:
            current_node.right = self.__r_insert(current_node.right, value)
        if current_node.value < value:
            current_node.left = self.__r_insert(current_node.left, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def contains(self, value):
        temp = self.root

        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def __r_contains(self, node, value):
        if node == None:
            return False
        if node.value == value:
            return True
        if node.value > value:
            return self.__r_contains(node.right, value)
        if node.value < value:
            return self.__r_contains(node.left, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None

        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        elif value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.right is None:
                current_node = current_node.left
            elif current_node.left is None:
                current_node = current_node.right
            else:
                bst_min_value = self.min_value(current_node.right)
                current_node.value = bst_min_value
                current_node.right = self.__delete_node(
                    current_node.right, bst_min_value)

        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def BFS(self):
        cureent_node = self.root
        queue = []
        result = []
        queue.append(cureent_node)
        while len(queue) > 0:
            cureent_node = queue.pop(0)
            result.append(cureent_node.value)
            if cureent_node.left:
                queue.append(cureent_node.left)
            if cureent_node.right:
                queue.append(cureent_node.right)
        return result

    def DFS_pre_order(self):
        result = []

        def travers(current_node):
            result.append(current_node.value)
            if current_node.left:
                travers(current_node.left)
            if current_node.right:
                travers(current_node.right)

        travers(self.root)
        return result

    def DFS_post_order(self):
        result = []

        def travers(current_node):
            if current_node.left:
                travers(current_node.left)
            if current_node.right:
                travers(current_node.right)
            result.append(current_node.value)

        travers(self.root)
        return result

    def DFS_inorder(self):
        result = []

        def travers(current_node):
            if current_node.left:
                travers(current_node.left)
            result.append(current_node.value)
            if current_node.right:
                travers(current_node.right)
        travers(self.root)
        return result

    def kth_smallest(self, kth):
        if self.root is None:
            return None
        if kth < 1:
            return None
        
        result = []
        def travers(current_node):
            if current_node.left:
                travers(current_node.left)
            result.append(current_node.value)
            if len(result) >= kth:
                return result[kth-1]
            if current_node.right:
                return travers(current_node.right)
            
        return travers(self.root)


bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7

# print(bst.BFS())
# print(bst.DFS_pre_order())
# print(bst.DFS_post_order())
# print(bst.DFS_inorder())
