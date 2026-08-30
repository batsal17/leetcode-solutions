class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a=1
        while num>=(a*a):
            if num==a*a:
                return True
            a=a+1
        return False
s1=Solution()
a=int(input("Enter a number: "))
if (s1.isPerfectSquare(a)):
    print(a,"is the perfect square")
else:
    print("Not a perfect square")