class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            return True
        temp = self.head
        new_node.next = temp
        self.head = new_node
        temp = None
        self.length += 1
        if self.length == 1:
            self.tail = new_node
        return True

    def pop(self):
        if (self.length == 0):
            return None

        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def remove_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            temp = self.remove_first()
            return temp

        if index == self.length-1:
            temp = self.pop()
            return temp

        pre = self.get(index-1)
        temp = pre.next

        pre.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp is None:
            return None
        temp.value = value
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
            
    def find_middle_node(self):
        slow=self.head
        fast=self.head
        
        while slow.next :
            slow=slow.next
            fast=fast.next.next
            if fast is None or fast.next is None:
                return slow
        return slow   
            
my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
print(my_linked_list.find_middle_node().value)
