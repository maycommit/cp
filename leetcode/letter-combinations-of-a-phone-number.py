import itertools
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if len(digits) == 1:
            return buttons[digits]

        letters = []
        for d in digits:
            letters.append(buttons[d])

        def btk(arr, i, j, res, c = []):
            c.append(arr[i][j])
            if j >= len(letters[i]) - 1:
                res.append("".join(c))
                return

            for j in range(len(arr[i])):
                btk(arr, aux, j, res, c)
                c.pop()

        res = []
        j = 0
        while j < len(digits):
            btk(letters, 0, j, res, [])
            j += 1

        return res

s = Solution()
print(s.letterCombinations("23"))
# print(s.letterCombinations(""))
# print(s.letterCombinations("2"))
# print(s.letterCombinations("234"))

