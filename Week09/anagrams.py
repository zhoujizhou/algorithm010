class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)
        if len_s < len_p:
            return []
        char_dict = {}
        win_dict = {}
        diff = len_p
        for ch in p:
            char_dict[ch] = char_dict.get(ch, 0) + 1
            win_dict[ch] = 0
        for i in range(len_p):
            if s[i] in win_dict:
                if win_dict[s[i]] < char_dict[s[i]]:
                    diff -= 1
                win_dict[s[i]] += 1
        p, q = 0, len_p - 1
        res = []
        if diff == 0:
            res.append(0)
        while q + 1 < len_s:
            q += 1
            if s[q] in win_dict:
                if win_dict[s[q]] < char_dict[s[q]]:
                    diff -= 1
                win_dict[s[q]] += 1
            if s[p] in win_dict:
                if win_dict[s[p]] <= char_dict[s[p]]:
                    diff += 1
                win_dict[s[p]] -= 1
            p += 1
            if diff == 0:
                res.append(p)
        return res
