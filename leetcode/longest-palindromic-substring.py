class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        table = [[0 for x in range(n)] for y in range(n)]

        max_length = 1
        i = 0
        while i < n:
            table[i][i] = True
            i += 1

        start = 0
        i = 0
        while i < n - 1:
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                max_length = 2
            i += 1

        k = 3
        while k <= n:
            i = 0
            while i < (n - k + 1):
                j = i + k - 1

                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True
                    if k > max_length:
                        start = i
                        max_length = k
                i += 1
            k += 1

        return s[start: start + max_length]

s = Solution()
s.longestPalindrome("babad")
s.longestPalindrome("cbbd")
