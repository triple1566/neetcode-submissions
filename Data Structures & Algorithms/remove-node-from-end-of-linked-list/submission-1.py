# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recursiveTrav(self, prev, head, n):
        # if reached the end, return 1
        if head == None:
            return [None,1]
        elif head != None:
            index = self.recursiveTrav(head, head.next, n)[1]
            if n == index:
                if prev != None:
                    prev.next = head.next
                    head.next = None
                    return [prev,index+1]
                elif prev == None:
                    tmp = head.next
                    head.next = None
                    head = None
                    return [tmp,index+1]
            return [head,index+1]

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Do it recursive
        # recursively traverse to the end of string.
        # back track and count nodes
        # Delete nth node and mend the list
        return self.recursiveTrav(None, head, n)[0]
    
