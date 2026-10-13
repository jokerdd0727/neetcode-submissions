# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        first = second = head
        while second and second.next:
            first = first.next
            second = second.next.next
        
        second = first.next # The head of second list 
        first.next = None # Split the first list from overall list
        prev = None # Preparing for swapping in list2
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first = head # Starting Node of list1
        second = prev # Starting Node of list2

        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            


            
        
        