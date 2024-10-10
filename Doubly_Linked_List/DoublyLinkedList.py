class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prv = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True

        self.tail.next = new_node
        new_node.prv = self.tail
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prv
            self.tail.next = None
            temp.prv = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.pre = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if self.length / 2 > index:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prv
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if self.length == index:
            return self.append(value)

        new_node = Node(value)
        befor = self.get(index-1)
        after = befor.next

        new_node.prv = befor
        new_node.next = after
        befor.next = new_node
        after.prv = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length -1:
            return self.pop()
        
        temp=self.get(index)
        temp.next.prv=temp.prv
        temp.prv.next=temp.next
        temp.next=None
        temp.prv=None
        self.length -=1
        return temp
        


my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(9)
my_doubly_linked_list.append(10)
print("removed item value is: ",my_doubly_linked_list.remove(5).value)
my_doubly_linked_list.print_list()
