class Solution:
    def reverseVowels(self, s):
        right=len(s)-1
        left=0
        sl=list(s)
        a='aeiouAEIOU'
        while right>left:
            if sl[right] not in a:
                right=right-1
            elif sl[left] not in a:
                left=left+1
            else:
                sl[right], sl[left]=sl[left], sl[right]
                right=right-1
                left=left+1
        return ''.join(sl)
s1=Solution()
print(s1.reverseVowels("leetcode"))          
