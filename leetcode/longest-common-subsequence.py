class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        b = [[0 for _ in range(0, n + 1)] for _ in range(0, m + 1)]
        c = [[0 for _ in range(0, n + 1)] for _ in range(0, m + 1)]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    c[i][j] = c[i - 1][j - 1] + 1
                    b[i][j] = "D"
                elif c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = "U"
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = "L"

        for i in range(m):
            print(c[i])

        def print_lcs(i, j):
            if i == 0 or j == 0:
                return
            if b[i][j] == "D":
                print_lcs(i - 1, j - 1)
                print(text1[i])
            elif b[i][j] == "U":
                print_lcs(i - 1, j)
            else:
                print_lcs(i, j - 1)

        print_lcs(m - 1, n - 1)


s = Solution()
s.longestCommonSubsequence("abcbdab", "bdcaba")