class Solution:
    def reverseString(self, s):
        right=len(s)-1
        left=0
        while right>left:
            s[right],s[left]=s[left],s[right]
            right=right-1
            left=left+1
        return s
s1=Solution()
print(s1.reverseString(["a","e","i","o","u"]))