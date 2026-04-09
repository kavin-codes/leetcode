class Solution:
    def pascel(self,rownums):

        row=[1]
        for i in range(1,rownums+1):
            new_row=[1]
            for j in range(1,i):
                new_row.append(row[j-1] + row[j])
            new_row.append(1)
            row=new_row
        return row 
    

rownums=1
s1=Solution()
print(s1.pascel(rownums)) 