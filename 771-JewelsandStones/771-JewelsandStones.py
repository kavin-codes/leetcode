#jewels = "aA"
#stones = "aAABbbb"

jewels = "z"      
stones = "ZZ"

class Solution:
    def single(self,jewels,stones):
        freq={}

        for i in jewels:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        
        count=0
        for ch in stones:
            if ch in freq:
                count+=1
        
        return count
            
s1=Solution()
print(s1.single(jewels,stones))

