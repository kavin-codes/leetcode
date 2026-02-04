words = ["abba","baba","bbaa","cd","cd"]

class solution:
    def single(self, words):

        
        
        
        res=[]
        prev=None
        
        for word in words:
            freq={}
            for ch in word:
                 if ch in freq:
                     freq[ch]+=1
                 else:
                     freq[ch]=1 


        
            if freq!=prev:
                res.append(word)
                prev=freq


        return res
           
s1= solution()
print(s1.single(words))
            