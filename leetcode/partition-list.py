# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res = []
        list = []
        max = x

        arr = [head]
        while (arr[-1].next != None):
            arr.append(arr[-1].next)

        while head != None:
            if head.val > max:
                max = head.val
            list.append(head.val)
            head = head.next

        i = 0
        while i < len(list):

            i += 1

        print(res, max)

s = Solution()
s.partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3)
s.partition(ListNode(2, ListNode(1)), 2)
