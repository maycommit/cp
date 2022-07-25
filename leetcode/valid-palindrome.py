class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        i = 0
        while i < len(s):
            if s[i].isalpha():
                tmp += s[i].lower()
            i += 1

        if len(tmp) <= 1:
            return False
        return tmp == tmp[::-1]


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
print(s.isPalindrome("0P"))
