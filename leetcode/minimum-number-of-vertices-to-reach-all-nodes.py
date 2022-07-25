from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        targets = set()

        for i in range(len(edges)):
            src, target = edges[i]
            targets.add(target)

        res = []
        for i in range(n):
            if i not in targets:
                res.append(i)

        print(res)
        return res


s = Solution()
s.findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]])
s.findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]])

