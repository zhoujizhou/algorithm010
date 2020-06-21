class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tempmap = {}
        for i in s:
            if i in tempmap:
                tempmap[i]+=1
            else:
                tempmap[i]=1
        
        for i in t:
            if i in tempmap:
                tempmap[i]-=1
            else:
                return False

        for i in tempmap.values():
            if i != 0 :
                return False
        
        return True

