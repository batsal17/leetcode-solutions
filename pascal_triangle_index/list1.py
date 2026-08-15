class Solution:
    def getRow(self, rowIndex):
        b=[]
        for i in range(0,rowIndex+1):
            b.append([0]*(i+1))
            b[i][0]=1
            b[i][i]=1
            for j in range(1,i):
                b[i][j]=b[i-1][j-1]+b[i-1][j]
        return b[rowIndex]
s1=Solution()
a=int(input("Enter rowIndex: "))
print(s1.getRow(a))