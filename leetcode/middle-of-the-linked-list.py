from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        print(arr[len(arr) // 2])

        return arr[len(arr) // 2]


s =  Solution()
s.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
s.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
