class Solution:
    def fib(self, n: int) -> int:

        fib_list = [0, 1]

        def util(num):
            if num < len(fib_list):
                return fib_list[num]
            else:
                fib_list.append(util(num - 1) + util(num - 2))

            return fib_list[num]

        return util(n)





s = Solution()
# print(s.fib(2))
# s.fib(3)
print(s.fib(4))
