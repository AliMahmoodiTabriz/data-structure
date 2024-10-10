class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    # def partition_list(self,x):
    #     up=LinkedList(0)
    #     down=LinkedList(0)
    #     up.make_empty()
    #     down.make_empty()
        
    #     temp=self.head
    #     while temp is not None:
    #         if temp.value >= x:
    #             up.append(temp.value)
    #         else:
    #             down.append(temp.value)
                
    #         temp=temp.next    
        
    #     self.make_empty()
        
    #     temp=down.head
    #     while temp is not None:
    #         self.append(temp.value)
    #         temp=temp.next
            
    #     temp=up.head
    #     while temp is not None:
    #         self.append(temp.value)
    #         temp=temp.next
            
        
            


def partition_list(self, x):
    # 1. Edge case: Check if the list is empty. If so, exit.
    if not self.head:
        return None
 
    # 2. Create two dummy nodes: 
    # dummy1 for nodes with values less than x 
    # and dummy2 for nodes with values greater or equal to x.
    dummy1 = Node(0)
    dummy2 = Node(0)
 
    # 3. Initialize two pointers (prev1 and prev2) at the dummy nodes.
    # They will be used to build the two separate lists.
    prev1 = dummy1
    prev2 = dummy2
 
    # 4. Start iterating from the head of the original list.
    current = self.head
 
    # 5. Traverse the entire list.
    while current:
        # 5.1. If the current node's value is less than x:
        if current.value < x:
            # 5.1.1. Attach it to the end of the list starting at dummy1.
            prev1.next = current
            # 5.1.2. Move the prev1 pointer forward.
            prev1 = current
        # 5.2. Otherwise:
        else:
            # 5.2.1. Attach it to the end of the list starting at dummy2.
            prev2.next = current
            # 5.2.2. Move the prev2 pointer forward.
            prev2 = current
        
        # 5.3. Move to the next node in the original list.
        current = current.next
 
    # 6. End the two lists. Set the next pointers of prev1 and prev2 to None.
    prev1.next = None
    prev2.next = None
 
    # 7. Link the end of the first list (the one that started at dummy1) 
    # to the beginning of the second list (the one that started at dummy2).
    prev1.next = dummy2.next
 
    # 8. Update the head of the linked list to point to the beginning 
    # of the partitioned list.
    self.head = dummy1.next


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0
    
    print("-----------------------")
    
    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()
      