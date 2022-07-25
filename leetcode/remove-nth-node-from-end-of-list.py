from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = [head]
        while(arr[-1].next != None):
            arr.append(arr[-1].next)

        arr.pop(-n)
        if len(arr) <= 0:
            return None

        if n - 1 == 0:
            arr[-n].next = None
        elif n <= len(arr):
            arr[-n].next = arr[-n + 1]

        return arr[0]



s = Solution()
s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
s.removeNthFromEnd(ListNode(1, ListNode(2)), 1)
s.removeNthFromEnd(ListNode(1, ListNode(2)), 2)

