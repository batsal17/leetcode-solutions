from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        a=Counter(s)
        b=Counter(t)
        if a==b:
            return True
        return False
s1=Solution()
c=input("Enter a word1: ")
d=input("Enter a word2: ")
if s1.isAnagram(c,d):
    print("They are anagrams.")
else:
    print("They are not anagrams.")