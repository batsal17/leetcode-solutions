class Solution:
    def addBinary(self, a, b):
        a1=len(a)
        b1=len(b)
        while a1!=b1:
            if a1<b1:
                a='0'+a
                a1=a1+1
            else:
                b='0'+b
                b1=b1+1
        summ=''
        carry='0'
        for i in range(len(a)-1,-1,-1):
            if a[i]=='0' and b[i]=='0':
                if carry=='0':
                    summ='0'+summ
                else:
                    summ='1'+summ
                    carry='0'
            elif a[i]!=b[i]:
                if carry=='0':
                    summ='1'+summ
                else:
                    summ='0'+summ
            else:
                if carry=='0':
                    summ='0'+summ
                    carry='1'
                else:
                    summ='1'+summ
        if carry=='1':
            summ='1'+summ
        return summ
s1=Solution()
j=input("Enter a binary string s1: ")
k=input("Enter a binary string s2: ")
print(s1.addBinary(j,k))

            

