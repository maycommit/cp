from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []
        count = 1

        while len(triangle) < numRows:
            i = len(triangle)
            row = []
            for j in range(count):
                if j == 0 or j == count - 1:
                    row.append(1)
                elif i > 1 and j > 0:
                    sum = triangle[i - 1][j] + triangle[i - 1][j - 1]
                    row.append(sum)

            triangle.append(row)
            count += 1

        print(triangle)
        return triangle

# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
s = Solution()
s.generate(5)
s.generate(1)
