# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        current = head
        #count the number of nodes in the linkee list 
        while current is not None:
            count += 1
            current = current.next
        mid = count // 2
        #now i have to print the nodes 
        current = head
        for _ in range(mid):
                current = current.next

        #returning a node and list is the same thing in leetcode it returns value and the next thing it points to
        return current
        
