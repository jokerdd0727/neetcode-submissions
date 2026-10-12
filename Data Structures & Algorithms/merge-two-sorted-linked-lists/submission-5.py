# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        New = ListNode()
        head = New
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                New.next = curr1
                curr1 = curr1.next
            else:
                New.next = curr2
                curr2 = curr2.next
            New = New.next

        if curr1: New.next = curr1
        if curr2: New.next = curr2
            
        return head.next