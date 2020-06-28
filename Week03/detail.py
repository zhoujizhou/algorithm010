class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.DFS( 1, k, n, [], res)
        return res

    def DFS(self,start, k, n, pre, res):
        if len(pre) == k :
            res.append(pre[:])
            return

        for i in range(start, n+1):
            pre.append(i)
            self.DFS(i+1,k,n,pre,res)
            pre.pop()
