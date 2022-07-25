from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = len(s) - 1
        while i >= 0:
            item = s.pop(0)
            s.insert(i, item)
            i -= 1


s =  Solution()
s.reverseString(["h","e","l","l","o"])
s.reverseString(["H","a","n","n","a","h"])


