class StackAsaList:
    def __init__(self):
        self.stack_list = []
        
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])


    def push(self,value):
        self.stack_list.append(value)
    
    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()


my_stack = StackAsaList()
my_stack.pop()

my_stack.print_stack()
