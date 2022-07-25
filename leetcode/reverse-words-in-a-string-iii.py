class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        words = s.split(" ")
        for word in words:
            res += word[::-1]
            res += " "

        return res.strip()


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverseWords("God Ding"))

