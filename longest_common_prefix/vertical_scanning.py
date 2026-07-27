from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c = ''
        e = 0
        while True and e < len(strs[0]):
            f = strs[0][e]
            d = 1
            match = True
            while True and d < len(strs):
                if e >= len(strs[d]) or f != strs[d][e]:
                    match = False
                    break
                d = d + 1
            if match == False:
                break
            c = c + f
            e = e + 1
        return c


s1 = Solution()
print(s1.longestCommonPrefix(["flower", "flow", "flight"])) 
print(s1.longestCommonPrefix(["dog", "racecar", "car"]))      