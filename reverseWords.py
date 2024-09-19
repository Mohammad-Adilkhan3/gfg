def reverseWords(self,str):
        # code here 
        s=str
        v=s.split(".")
        res='.'.join(v[::-1])
        return res
