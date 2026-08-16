class Solution:
    def isHappy(self, n):
        a=n
        s=0
        b=[]
        while n not in b:
            b.append(n)
            while a>0:
                r=a%10
                s=s+r**2
                a=a//10
            n=s
            a=n
            s=0
        print(b)
        if n==1:
            return True
        return False
s1=Solution()
o=int(input("Enter a number: "))
if s1.isHappy(o):
    print("It's a happy number")
else:
    print("Not")