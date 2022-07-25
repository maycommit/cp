from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1


        def dfs(node, res, path = []):
            path.append(node)

            if node == target:
                res.append([p for p in path])
            else:
                for c in graph[node]:
                    dfs(c, res, path)

            path.pop()

        res = []
        dfs(0, res)

        return res



s = Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
