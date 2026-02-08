s="abccccdd"

class Solution:
    def single(self, s):

        freq ={}

        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1

        length =0
        odd_found =False

        for count in freq.values():
            if count%2==0:
                length+=count
            else:
                length+=count-1
                odd_found=True

        if odd_found:
            length+=1

        return length   

    #or 

    """
        seen = set()
        length = 0
        
        for ch in s:
            if ch in seen:
                seen.remove(ch)
                length += 2
            else:
                seen.add(ch)
        
        # If any leftover chars exist, one can go in the center
        if seen:
            length += 1
        
        return length""" 
    
s1=Solution()
print(s1.single(s))








        