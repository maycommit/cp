# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
pos = 1
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list = [head]
        while list[-1].next != None:
            list.append(list[-1].next)

        print(list)

s = Solution()
head = ListNode(3)
first = ListNode(2)
second = ListNode(0)
three = ListNode(-4)

head.next = first
first.next = second
second.next = three
three.next = second

s.hasCycle(head)