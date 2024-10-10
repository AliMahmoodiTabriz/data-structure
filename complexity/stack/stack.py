class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next=self.top
            self.top=new_node
        
        self.length+=1
        return True    
    
    def pop(self):
        if self.length == 0:
            return None
        temp=self.top
        
        if self.length==1:
            self.top=None
        else:
              self.top=self.top.next
              temp.next=None
        self.length-=1
        return temp

my_stack = Stack(0)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.pop()
my_stack.print()
