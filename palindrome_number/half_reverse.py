class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        reverse=0
        while x>reverse:
            reverse=reverse*10+x%10
            x=x//10
        return x==reverse or x==reverse//10

s1=Solution()
a=int(input("Enter a number to check if it's palindrome or not: "))
print(s1.isPalindrome(a))