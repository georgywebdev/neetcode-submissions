# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next   # save where we're headed next
            curr.next = prev        # reverse the current link
            prev = curr             # advance prev
            curr = next_temp        # advance curr
        return prev