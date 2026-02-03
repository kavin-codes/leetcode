ransomNote = "a"
magazine = "b"

 
class Solution:
   def single(self, ransomNote, magazine  ):
      d1={}
      d2={}
      
      for i in ransomNote: 
         if i in d1:
            d1[i]+=1
         else:
            d1[i]=1
         
      
    

      for j in magazine : 
         if j in d2:
            d2[j]+=1
         else:
            d2[j]=1
            

      for ch in d1:
            if ch not in d2 or d2[ch] < d1[ch]:
                return False
         
      return True

   
s1=Solution()
print(s1.single(ransomNote,magazine))