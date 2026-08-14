class Solution:
    def generate(self, numRows):
        b=[]
        for i in range(0,numRows):
            b.append([0]*(i+1))
            b[i][0]=1
            b[i][i]=1
            for j in range(1,i):
                b[i][j]=b[i-1][j-1]+b[i-1][j]
        return b
s1=Solution()
x=int(input("Enter number of rows: "))
print(s1.generate(x))