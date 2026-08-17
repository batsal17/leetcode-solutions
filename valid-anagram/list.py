class Solution:
    def isAnagram(self, s, t):
        a=list(s)
        b=list(t)
        if len(a)==len(b):
            for i in a:
                if i in b:
                    b.remove(i)
            if len(b)==0:
                return True
        return False
s1=Solution()
c=input("Enter a word1: ")
d=input("Enter a word2: ")
if s1.isAnagram(c,d):
    print("They are anagrams.")
else:
    print("They are not anagrams.")