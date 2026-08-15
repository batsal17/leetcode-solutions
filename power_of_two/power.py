class Solution:
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        a=0
        while 2**a<=n:
            if 2**a==n:
                return True
            a=a+1
        return False
s1=Solution()
a=int(input("Enter a number: "))
if s1.isPowerOfTwo(a):
    print("It is a power of 2")
else:
    print("It is not the power of 2")