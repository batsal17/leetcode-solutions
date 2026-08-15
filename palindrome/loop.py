class Solution:
    def isPalindrome(self, s):
        a=''.join(char for char in s if char.isalnum()).lower()
        b=''
        for i in a:
            b=i+b
        return a==b
s1=Solution()
c=input("Enter a sentence: ")
if s1.isPalindrome(c):
    print("Palindrome")
else:
    print("Not Palindrome")