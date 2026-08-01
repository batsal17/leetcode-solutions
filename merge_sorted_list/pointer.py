# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode()
        temp=dummy
        while list1 and list2:
            if list1.val<list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        if list1:
            temp.next=list1
        else:
            temp.next=list2
        return dummy.next

a = ListNode(1)
a.next = ListNode(3)
a.next.next = ListNode(5)

b = ListNode(2)
b.next = ListNode(4)
b.next.next = ListNode(6)

s1 = Solution()
result = s1.mergeTwoLists(a, b)

while result:
    print(result.val, end="")
    
    if result.next:
        print(" → ", end="")
    
    result = result.next