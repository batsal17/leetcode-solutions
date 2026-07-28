class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return 0

        left = 1
        right = x // 2
        s = 1

        while left <= right:
            i = (left + right) // 2

            if i * i == x:
                return i

            if i * i < x:
                s = i
                left = i + 1

            else:
                right = i - 1

        return s

s1=Solution()
x=int(input("Enter a number: "))
print(s1.mySqrt(x))