class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, r
            r = p + q
        return r
      

if __name__=="__main__":
    n = 4
    method = Solution()
    answer = method.fib(n)
    print(answer)