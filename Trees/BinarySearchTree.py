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

        if value > current_node.value :
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


my_BST = BinarySearchTree()
my_BST.insert(47)
my_BST.insert(21)
my_BST.insert(76)
my_BST.insert(18)
my_BST.insert(27)
my_BST.insert(52)
my_BST.insert(82)
my_BST.delete_node(18)
print(my_BST.min_value(my_BST.root))
#print(my_BST.min_value(my_BST.root.right))
