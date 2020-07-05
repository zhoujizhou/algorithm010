class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count=0

        while True:
            if not g or not s:
                return count
            elif g[-1]>s[-1]:
                g.pop()
            else:
                g.pop()
                s.pop()
                count+=1
