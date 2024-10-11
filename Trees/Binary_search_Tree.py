class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_search_Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
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

    def contain(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

        return False


my_tree = Binary_search_Tree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# print("root value is: ", my_tree.root.value)
# print("left value is: ", my_tree.root.left.value)
# print("right value is: ", my_tree.root.right.value)
print("right value is: ", my_tree.contain(82))
