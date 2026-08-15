class Solution:
    def isPalindrome(self, s):
        a=''.join(char for char in s if char.isalnum()).lower()
        if a==a[::-1]:
            return True
        else:
            return False
s1=Solution()
b=input("Enter a sentence: ")
if s1.isPalindrome(b):
    print("Palindrome")
else:
    print("Not Palindrome")