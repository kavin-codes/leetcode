s = "a#c"
t = "b"



class solution:
    def backspace(self,s,t):
        st=[]
        stc=[]
        
        for c in s:
            if c=="#":
                if st!=[]:
                     st.pop()
            else:
                st.append(c)

               
           
                
        SUM1= "".join(st)
        
        
        for a in t:
            if a=="#":
                if stc!=[]:
                    stc.pop()
            else:
                stc.append(a)

                
           
                
        SUM2="".join(stc)
    
        if  SUM1==SUM2:
            return True
        else:
            return False
    
s1=solution()
print(s1.backspace(s,t))

