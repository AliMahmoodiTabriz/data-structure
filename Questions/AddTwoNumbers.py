from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    queue1 = []
    queue2 = []
    strL1 = ""
    strL2 = ""
    while l1:
        queue1.append(l1)
        l1 = l1.next

    while l2:
        queue2.append(l2)
        l2 = l2.next

    while len(queue1) > 0:
        strL1 += str(queue1.pop().val)

    while len(queue2) > 0:
        strL2 += str(queue2.pop().val)
    sum = int(strL1) + int(strL2)

    head = ListNode(int(str(sum)[len(str(sum))-1]))
    temp = head
    for i in range(len(str(sum))-2, -1, -1):
        temp.next = ListNode(int(str(sum)[i]))
        temp = temp.next

    return head


def addTwoNumber(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0) 
    current = dummy
    carry = 0 

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0 
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10 
        current.next = ListNode(total % 10)
        current = current.next  

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next 

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(9)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)
head = addTwoNumber(l1, l2)
while head:
    print(head.val)
    head = head.next
